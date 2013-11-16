from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'home.views.index', name='index'),
  url(r'^questions/', include('questions.urls')),

  url(r'^admin/', include(admin.site.urls)),
)
