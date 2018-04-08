from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from polls.models import Question, Choice
from blog.models import Article, Category
from podcast.models import Podcast
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime

def home(request):
    latest_question_list = Question.objects.order_by('-created')[:2]
    top_article = Article.objects.order_by('-pub_date')[:1]
    article_list = Article.objects.order_by('-pub_date')[1:5]
    podcast_list = Podcast.objects.order_by('-pub_date')
    now = datetime.datetime.now()
    context = {
        'latest_question_list':latest_question_list,
        'article_list':article_list,
        'top_article':top_article,
        'podcast_list':podcast_list,
        'now':now
    }
    return render(request, 'home/home.html', context)
