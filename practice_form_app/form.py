
from django import forms
from django.core import validators

class practice_form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your name'}),validators=[validators.MinLengthValidator(10,message='your name at lest 10 chars')])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='You must be use .com')])
    password = forms.CharField(widget=forms.PasswordInput)
    newPassword = forms.CharField(widget=forms.PasswordInput,label='confirm Password')
    
    def clean(self):
        cleaned_data = super().clean()
        currentPass = self.cleaned_data['password']
        newpass = self.cleaned_data['newPassword']
        if currentPass != newpass:
            raise forms.ValidationError("Password don't match")
        