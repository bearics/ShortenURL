from django import forms


class SendUrlForm(forms.Form):
    original_url = forms.CharField(max_length=50)
