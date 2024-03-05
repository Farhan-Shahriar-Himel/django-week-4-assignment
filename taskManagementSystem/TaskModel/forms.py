from django import forms 
from .models import TaskModel 

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        widgets = {
            'taskAssignDate' : forms.DateInput(attrs={'type':'date'})
        }