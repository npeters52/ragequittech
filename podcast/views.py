# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Podcast, Channel
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

# def podcast_index(request):
#     podcast_archive_list = Podcast.objects.filter(is_published=True).order_by('-pub_date')
#     context = {
#         'podcast_archive_list': podcast_archive_list
#     }
#     return render(request, 'podcast/podcast_index.html', context)

def podcast_index(request):
    podcast_archive_list = Podcast.objects.order_by('-pub_date')
    paginator = Paginator(podcast_archive_list, 10)
    page = request.GET.get('page', 1)
    try:
        paginated_podcasts = paginator.page(page)
    except PageNotAnInteger:
        paginated_podcasts = paginator.page(1)
    except EmptyPage:
        paginated_podcasts= paginator.page(paginator.num_pages)
    context = {
        'podcast_archive_list':paginated_podcasts
    }
    return render(request, 'podcast/podcast_index.html', context)

def podcast_detail(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)
    return render(request, 'podcast/podcast_detail.html', {'podcast':podcast})
