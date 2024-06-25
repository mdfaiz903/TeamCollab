from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


    
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='members')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.project

STATUS_CHOICE = [('to_do', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')]
PRIORITY_CHOICE = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]
class Task(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICE)
    assigned_to = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.task
