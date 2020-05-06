from django import forms
# Create your views here.


class HomeForm(forms.Form):
    post = forms.CharField()
