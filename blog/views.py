from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Category
from django.template import loader
from django.urls import reverse

# Create your views here.

def articles(request):
    article_list = Article.objects.order_by(-pub_date)[:10]
    context = {
        'article_list':article_list
    }
    return render(request, 'blog/blog_index.html', context )

def post(request):
    post = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/blog_post', {'post':post})
