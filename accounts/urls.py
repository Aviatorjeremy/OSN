from django.conf.urls import patterns
from accounts.views import Registration, Login, Logout, Settings, SetProfile

urlpatterns = patterns('',
    (r'^registration/$',Registration.as_view()),
    (r'^login/$', Login.as_view()),
    (r'^logout/$', Logout.as_view()),
    (r'^settings/$', Settings.as_view()),
    (r'^settings/profile/$', SetProfile.as_view()),
)