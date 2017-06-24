# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Channel(models.Model):
    name = models.CharField(max_length=300)

class Podcast(models.Model):
    name = models.CharField(max_length=300)
    link = models.URLField()
    author = models.ForeignKey(User, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
