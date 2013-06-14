from datetime import datetime

from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
# from django.views.generic.edit import FormView
from accounts.models import MyUser as User
from newpo.forms import TweetForm
from newpo.models import (
    Message,
    Comment,
)

class PostView(View):
    def get(self, request):
        form = TweetForm()
        msg = Message.objects.all() ## need to be revized!
        return render(request, 'newpo/home.html', {'form':form, 'msg':msg})
    def post(self, request):
        msg = Message(user=User.objects.get(pk=int(request.session['member_id'])), time_published=datetime.now(),tweet=request.POST['tweet'])
        msg.save()
        return redirect('/dashboard')