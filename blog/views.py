from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Category
from django.template import loader
from django.urls import reverse

# Create your views here.

def articles(request):
    archive_list = Article.objects.order_by('-pub_date')[:10]
    context = {
        'archive_list':archive_list
    }
    return render(request, 'blog/blog_archive.html', context )

def blogpost(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/blog_post.html', {'article':article})
