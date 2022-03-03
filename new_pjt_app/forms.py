from django import forms
from django.forms import ModelForm
from new_pjt_app.models import first_model

class User_Form(ModelForm):
    class Meta:
        model = first_model
        fields = "__all__"