from django.db import models
from accounts.models import User
# Create your models here.

class ContentCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)

class Content(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.CharField(max_length=60)
    documents = models.FileField(upload_to="documents")
    category = models.ManyToManyField(ContentCategory,related_name='category_contents')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_contents')
