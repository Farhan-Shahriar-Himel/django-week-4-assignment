from django.shortcuts import render, redirect
from . import forms 
from . import models
# Create your views here.
def addTask(request):
    if request.method == 'POST':
        form = forms.TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')

    form = forms.TaskModelForm()
    return render(request, 'task.html', {'form': form})

def edit(request, id):
    data= models.TaskModel.objects.get(pk=id)
    form = forms.TaskModelForm(instance=data)
    if request.method == 'POST':
        form = forms.TaskModelForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'task.html', {'form': form})


def delete(request, id):
    data = models.TaskModel.objects.get(pk=id)
    data.delete()
    return redirect('homepage')
