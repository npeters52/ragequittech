from django.conf.urls import url

from . import views

app_name = 'podcast'
urlpatterns = [
    url(r'^$', views.podcast_index, name='podcast_index'),
    url(r'^(?P<podcast_id>[0-9]+)/$', views.podcast_detail, name='podcast_detail')
]
