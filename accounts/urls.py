from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns
from accounts.views import Registration, Login, Logout, Settings, SetProfile

urlpatterns = patterns('',
    (r'^registration/$',Registration.as_view()),
    (r'^login/$', Login.as_view()),
    (r'^logout/$', Logout.as_view()),
    (r'^settings/$', login_required(Settings.as_view())),
    (r'^settings/profile/$', login_required(SetProfile.as_view())),
)