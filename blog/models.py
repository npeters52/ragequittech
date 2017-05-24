from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=300)
    is_published = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    pub_date = models.DateTimeField('publish date')
    author = models.ForeignKey(User, null=True, blank=True)
    content = models.CharField(max_length=10000)
    image = models.FileField()

class Category(models.Model):
    name = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)