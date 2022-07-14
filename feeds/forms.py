from django import forms
from .models import MyModel
from django.forms import ModelForm, TextInput, EmailInput
class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["Full_Name", "Email","Subject","Messages"]
    labels = {'Full_Name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;color:white;',
                'placeholder': 'Name'
                }), "Email":  EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 600px;color:white;',
                'placeholder': 'Email'
                }),"Subject": TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;color:white;',
                'placeholder': 'Subject'
                }),"Messages": TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;color:white;',
                'placeholder': 'Messages'
                })}