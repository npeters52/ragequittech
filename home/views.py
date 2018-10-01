from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from polls.models import Question, Choice
from blog.models import Article, Category
from podcast.models import Podcast
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime
from django.shortcuts import render_to_response
from itertools import chain
import operator
from django.db.models import Q

def home(request):
    latest_question_list = Question.objects.order_by('-created')[:2]
    top_article = Article.objects.order_by('-pub_date')[:1]
    article_list = Article.objects.order_by('-pub_date')[1:4]
    podcast_list = Podcast.objects.order_by('-pub_date')[:3]
    now = datetime.datetime.now()
    context = {
        'latest_question_list':latest_question_list,
        'article_list':article_list,
        'top_article':top_article,
        'podcast_list':podcast_list,
        'now':now
    }
    return render(request, 'home/home.html', context)

# def search(request):
#     query_string = ''
#     found_entries = None
#     if ('q' in request.GET) and request.GET['q'].strip():
#         query_string = request.GET['q']

#         entry_query = get_query(query_string, ['title', 'body',])

#         found_entries = Article.objects.filter(entry_query).order_by('-pub_date')

#     context = {
#         'query_string': query_string, 
#         'found_entries': found_entries
#     }

#     return render(request, 'home/search_results.html', context)

def search(request):
    query = request.GET.get("q")

    article_queryset_list = Article.objects.all()

    podcast_queryset_list = Podcast.objects.all()

    combined_queryset_list = sorted(
        chain(article_queryset_list, podcast_queryset_list),
        key=lambda post: post.pub_date, reverse=True)

    if query:
        combined_queryset_list = sorted(combined_queryset_list, key=operator.attrgetter(
            Q(content__icontains=query) |
            Q(title__icontains=query) |
            Q(name__icontains=query)
        )).distinct()

    context = {
        "archive_list":combined_queryset_list
    }
    return render(request, 'blog/blog_archive.html', context)
