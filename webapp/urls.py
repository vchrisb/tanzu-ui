from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #TKGi
    path('cluster', views.cluster, name='cluster'),
    path('cluster/<pk>/kubeconfig', views.cluster_kubeconfig, name='cluster_kubeconfig'),
    path('cluster/<pk>/delete', views.cluster_delete, name='cluster_delete'),
    path('cluster/refresh', views.cluster_refresh, name='cluster_refresh'),
    path('cluster/create', views.ClusterCreate.as_view(), name='cluster_create'),
    #TAS
    path('organization', views.organization, name='organization'),
    path('organization/<pk>/delete', views.organization_delete, name='organization_delete'),
    path('organization/create', views.OrganizationCreate.as_view(), name='organization_create'),
]