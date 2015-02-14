from django.conf.urls import patterns, include, url
import blog

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^article_update/$', 'blog.views.article_update', name='article_update'),
    url(r'^comment_update/$', 'blog.views.comment_update', name='comment_update'),
    url(r'^article_remove/$', 'blog.views.article_remove', name='article_remove'),
    url(r'^comment_remove/$', 'blog.views.comment_remove', name='comment_remove'),
)