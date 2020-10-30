from django import forms

class ClusterForm(forms.Form):
    uuid = forms.UUIDField(label='UUUID')