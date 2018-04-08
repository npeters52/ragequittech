from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /polls
    url(r'^$', views.archive, name='archive'),
    # ex: /polls/5/
    url(r'^(?P<article_id>[0-9]+)/$', views.blogpost, name='blogpost'),
]
