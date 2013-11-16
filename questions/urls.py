from django.conf.urls import patterns, include, url

urlpatterns = patterns('questions.views',
  url(r'^$', 'index', name='home'),
  url(r'^novo$', 'create', name='create'),
)