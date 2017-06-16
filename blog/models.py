from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=300)
    is_published = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    pub_date = models.DateTimeField('publish date')
    author = models.ForeignKey(User, null=True, blank=True)
    content = models.CharField(max_length=10000)
    image = models.FileField(null=True, blank=True)
    slug = models.SlugField(max_length=40, default=None)

    def was_published_recently(self):
        """
        method for returning articles posted within the last day
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name