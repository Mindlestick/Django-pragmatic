from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    #누가 썼는지
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article',null=True)

    #어느 게시판인지
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article',null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)