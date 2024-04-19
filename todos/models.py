from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Project(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Todo(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
    )

    project = models.ForeignKey(Project, related_name='todos', on_delete=models.CASCADE)
    todoitem=models.CharField(max_length=100, null=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.description