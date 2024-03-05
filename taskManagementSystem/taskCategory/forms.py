from django import forms 
from . import models

class categoryForm(forms.ModelForm):
    class Meta:
        model = models.taskCategory
        fields = '__all__'