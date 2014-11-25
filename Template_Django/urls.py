from django.conf.urls import patterns, include, url
from django.contrib import admin

from Template_Django.views import index
from hackathon.views import signin, signup, logout, home, profile

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name='index'),
    url(r'^signin', signin, name='signin'),
    url(r'^signup', signup, name='signup'),
    url(r'^logout', logout, name='logout'),
    url(r'^home$', home, name='home'),
    url(r'^accounts/profile', profile, name='profile'),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
