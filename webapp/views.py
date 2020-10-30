from django.shortcuts import render, redirect
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from django.contrib.auth.decorators import login_required
from .models import Cluster
from django.conf import settings
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
import yaml
from .forms import ClusterForm

def index(request):
    return render(request, 'webapp/index.html')

@login_required
def cluster(request):
    clusters = Cluster.objects.filter(owner=request.user)
    context = {
        'clusters': clusters,
    }
    return render(request, 'webapp/cluster.html', context)

@login_required
def cluster_kubeconfig(request, pk=None):
    cluster = Cluster.objects.filter(owner=request.user).filter(uuid=pk).first()
    if(cluster):
      oauth = get_request_object()
      cluster_response = oauth.get("{}/v1/clusters/{}/binds/admin".format(settings.TKGI_API_URL, cluster.name))
      if(cluster_response.status_code == 200):
        response = HttpResponse(yaml.dump(cluster_response.json()), content_type='text/plain; charset=utf8')
        response['Content-Disposition'] = 'attachment; filename="kubeconfig"'
        return response
      else:
        print("binds not found")
    else:
      print("not found")
    return redirect("cluster")

@login_required
def cluster_refresh(request):
    clusters = Cluster.objects.filter(owner=request.user)
    oauth = get_request_object()

    for cluster in clusters:
      cluster_response = oauth.get("{}/v1/clusters/{}".format(settings.TKGI_API_URL, cluster.name))
      if(cluster_response.status_code == 200):
        current_cluster = cluster_response.json()
        cluster.last_action = current_cluster["last_action"]
        cluster.last_action_state = current_cluster["last_action_state"]
        cluster.last_action_description = current_cluster["last_action_description"]
        cluster.kubernetes_master_host = current_cluster["parameters"]["kubernetes_master_host"]
        cluster.save()
      elif(cluster_response.status_code == 404):
        cluster.delete()
      else:
        print("not found")
  
    return redirect("cluster")

@login_required
def cluster_delete(request, pk=None):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClusterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cluster = Cluster.objects.filter(owner=request.user).filter(uuid=pk).first()
            if(cluster):
              oauth = get_request_object()
              cluster_response = oauth.delete("{}/v1/clusters/{}".format(settings.TKGI_API_URL, cluster.name))
              if(cluster_response.status_code == 204):
                # redirect to a new URL:
                return redirect("cluster_refresh")
              else:
                error = "Error deleting Cluster {}".format(pk)
            else:
              error = "Cluster {} not found or does not belong to user".format(pk)
            return render(request, 'webapp/error.html', {'error': error})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClusterForm({'uuid': pk})

    return render(request, 'webapp/cluster_delete.html', {'form': form})

class ClusterCreate(LoginRequiredMixin, CreateView):
    model = Cluster
    fields = ['name']
    template_name = 'webapp/cluster_create.html'
    success_url = reverse_lazy("cluster")

    def form_valid(self, form):
        oauth = get_request_object()
        content = {
          'name': form.instance.name,
          'parameters': {
            'kubernetes_master_host': "{}.cluster.pks.colton.cf-app.com".format(form.instance.name),
            'kubernetes_master_port': 8443
          },
          'plan_name': 'small'
        }
        cluster_response = oauth.post("{}/v1/clusters".format(settings.TKGI_API_URL, ),json=content)
        if(cluster_response.status_code == 202):
          cluster = cluster_response.json()
          form.instance.owner = self.request.user
          current_cluster = cluster_response.json()
          form.instance.last_action = current_cluster["last_action"]
          form.instance.last_action_state = current_cluster["last_action_state"]
          form.instance.last_action_description = current_cluster["last_action_description"]
          form.instance.kubernetes_master_host = current_cluster["parameters"]["kubernetes_master_host"]
          form.instance.uuid = current_cluster["uuid"]
          form.instance.plan_name = current_cluster["plan_name"]
          return super().form_valid(form)
        else:
          form.add_error('name', "Failed to create cluster")
          return super().form_invalid(form)

def get_request_object():
    token_url = settings.TKGI_UAA_URL + '/oauth/token'
    client = BackendApplicationClient(client_id=settings.TKGI_CLIENT_ID)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, client_id=settings.TKGI_CLIENT_ID, client_secret=settings.TKGI_CLIENT_SECRET)
    return oauth