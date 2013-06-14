from django.conf.urls import patterns, url

from newpo.views import TweetView

urlpatterns = patterns('',
    url(r'^$', TweetView.as_view()),
    url(r'^tweet$',TweetView.as_view()),
    # url(r'^photo$', PhotoView.as_view()),
    # url(r'^blog$', BlogView.as_view()),
)