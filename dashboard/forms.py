from django import forms

class User(forms.Form):
    email = forms.CharField(label='email', max_length=10)
    pw = forms.CharField(label='pw', max_length=10)