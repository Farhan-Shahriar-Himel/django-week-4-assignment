from django.db import models
from taskCategory.models import taskCategory
# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.CharField(max_length=100)
    isCompleted = models.BooleanField(default=False)
    taskAssignDate = models.DateField()
    taskCategory = models.ManyToManyField(taskCategory)

    def __str__(self) -> str:
        return self.taskTitle