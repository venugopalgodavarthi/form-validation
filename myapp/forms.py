from django import forms

class log(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
