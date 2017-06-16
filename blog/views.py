from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def blog_index(request):
    latest_blog_list = Article.objects.order_by('-pub_date')[:5]
    context = {
        'latest_blog_list':latest_blog_list
    }
    return render(request, 'blog/blog_index.html', context)

def blog_detail(request, question_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/blog_detail.html', {'article':article})