from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Question(models.Model):
    """
    data fields for the questions
    """
    question_text = models.CharField(max_length=200)
    created = models.DateTimeField('date published')
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def was_published_recently(self):
        """
        method for returning questions posted within the last day
        """
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    """
    data fields for the choices
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    