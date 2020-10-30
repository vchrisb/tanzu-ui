from django.contrib import admin
from .models import Cluster

# Register your models here.
@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    pass