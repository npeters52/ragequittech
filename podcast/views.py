# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Podcast, Channel

# Create your views here.

def podcast_index(request):
    podcast_archive = Podcast.objects.filter(is_published=True).order_by('-pub_date')
    context = {
        'podcast_archive':podcast_archive
    }
    return render(request, 'podcast/podcast_index.html', context)

def podcast_detail(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)
    return render(request, 'podcast/podcast_detail.html', {'podcast':podcast})
