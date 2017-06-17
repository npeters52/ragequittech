from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls
    url(r'^$', views.articles, name='articles'),
    # ex: /polls/5/
    url(r'^(?P<article_id>[0-9]+)/$', views.post, name='post'),
]
