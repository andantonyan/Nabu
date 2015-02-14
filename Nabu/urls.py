from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from utils.models import Menu
import home, utils, account, blog

urlpatterns = patterns('',
    url(r'^$', 'home.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'account.views.login', name='login'),
    url(r'^logout/$', 'account.views.logout', name='logout'),
    url(r'^settings/$', 'account.views.settings', name='settings'),
    url(r'^registration/$', 'account.views.registration', name='registration'),
    url(r'^thanks/$', 'account.views.thanks', name='thanks'),
    url(r'^activate/(?P<email>.*)/$', 'account.views.activate', name='activate'),

    # blog
    url(r'^blog/', include('blog.urls' , namespace='blog')),

    # Docs
    url(r'^(?P<menu>.*)/(?P<submenu>.*)/$', 'utils.navigation.submenu', name='submenu'),
    url(r'^(?P<menu>.*)/$', 'utils.navigation.menu', name='menu'),
)

handler404 = 'utils.views.view_404'
urlpatterns += staticfiles_urlpatterns()

