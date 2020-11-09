from django.contrib import admin
from .models import Cluster, Organization

# Register your models here.
@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    pass

# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    pass