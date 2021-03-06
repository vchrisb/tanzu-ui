from django.db import models
import uuid
from django.conf import settings

# Create your models here.
class Cluster(models.Model):
    """
    A model which holds information about a particular Cluster
    """

    plans = [
        ('small', 'A small plan'),
        ('medium', 'A medium plan'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.SlugField(max_length=32, unique=True)
    plan_name = models.SlugField(choices=plans, max_length=32)
    uuid = models.UUIDField()
    last_action = models.CharField(max_length=100)
    last_action_state = models.CharField(max_length=100)
    last_action_description = models.CharField(max_length=200)
    kubernetes_master_host = models.CharField(max_length=200)
    kubernetes_master_port = models.IntegerField()
    kubernetes_master_ip = models.CharField(max_length=20, blank=True)
    kubernetes_worker_instances = models.IntegerField()
    k8s_version = models.CharField(max_length=30)


    def __str__(self):
        return self.name

# Create your models here.
class Organization(models.Model):
    """
    A model which holds information about a particular Organization
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.SlugField(max_length=32, unique=True)
    uuid = models.UUIDField()

    def __str__(self):
        return self.name