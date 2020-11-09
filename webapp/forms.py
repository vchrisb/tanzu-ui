from django import forms

class ClusterForm(forms.Form):
    uuid = forms.UUIDField(label='UUID')

class OrganizationForm(forms.Form):
    uuid = forms.UUIDField(label='UUID')