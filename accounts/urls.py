from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^registration/$','accounts.views.registration'),
	url(r'^login/$', 'accounts.views.login'),
	url(r'^settings/$', 'accounts.views.settings'),
)