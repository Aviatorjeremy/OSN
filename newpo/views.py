from datetime import datetime

from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from newpo.forms import TweetForm
from newpo.models import (
    Message,
    Comment,
)

def home_handlr(request):
    ## need to be revised!
    m = Message.objects.all() 
    render('newpo/home.html',{'message':m})

class TweetView(View):
    form_class = TweetForm
    # initial = {'key': 'value'}
    template_name = 'newpo/home.html'
    ## need to be revised!
    message = Message.objects.all() 
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request,  self.template_name, {'form': form, 'message':self.message})
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form_class = self.form_class(request.POST)
        if form.is_valid():
            m = Message(user=request.user, time_published=datetime.now(), tweet=form.tweet)
            m.save()
        return redirect('/dashboard')
