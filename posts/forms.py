from django import forms
from .import models



class Add_Post(forms.ModelForm):
    class Meta:
        model=models.Post
        exclude=['author']