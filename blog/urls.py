from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /polls
    url(r'^$', views.blog_index, name='blogIndex'),
    # ex: /polls/5/
    url(r'^blog/(?P<slug>[\w-]+)/$', views.blog_detail, name='blogDetail'),
]