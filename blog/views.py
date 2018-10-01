from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Category
from django.template import loader
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def articles(request):
    article_list = Article.objects.order_by('-pub_date')
    context = {
        'article_list':article_list
    }
    return render(request, 'blog/blog_index.html', context)

def blogpost(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/blog_post.html', {'article':article})

def archive(request):
    archive_list = Article.objects.order_by('-pub_date')
    paginator = Paginator(archive_list, 10)
    page = request.GET.get('page')
    paginated_articles = paginator.get_page(page)
    context = {
        'archive_list':paginated_articles
    }
    return render(request, 'blog/blog_archive.html', context)
