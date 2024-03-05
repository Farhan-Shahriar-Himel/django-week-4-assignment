from django.shortcuts import render
from TaskModel.models import TaskModel
from taskCategory.models import taskCategory

def home(request):
    data = TaskModel.objects.all()
    cat = taskCategory.objects.all()
    return render(request, 'home.html', {'data': data, 'category': cat})