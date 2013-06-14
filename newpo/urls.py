from django.conf.urls import patterns, url

from newpo.views import PostView

urlpatterns = patterns('',
    url(r'^$', PostView.as_view()),
    url(r'^tweet$', PostView.as_view()),
    # url(r'^photo$', PhotoView.as_view()),
    # url(r'^blog$', BlogView.as_view()),
)