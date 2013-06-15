from django.shortcuts import render, redirect
from django.forms import EmailField
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.views.generic.base import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from accounts.models import MyUser, UserProfile


class Registration(View):
    """
    registration
    """
    def get(self,request):
        return render(request, 'accounts/regist.html')
    
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        udomain = request.POST['udomain']
        if password and isEmailAddressValid(email):
            result = MyUser.objects.create_user(email, password, udomain)
        else:
            return render(request, 'accounts/regist.html')
        return render(request, 'accounts/success.html')

class Login(View):
    """
    lgoin
    """
    def get(self, request):
        next = request.GET.get('next',None)
        return render(request, 'accounts/login.html', {'next': next})

    def post(self, request):

        email = request.POST['email']
        password = request.POST['password']
        next = request.POST.get('next',None)
        user = auth.authenticate(email = email, password = password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if next != 'None':
                return redirect(next)
            return render(request, 'accounts/success.html', {'session':request.user} )
        else:
            return render(request, 'accounts/login.html')


class Logout(View):
    """
    Logout
    """
    def get(self, request):
        auth.logout(request)
        return render(request, 'accounts/success.html',{'session':request.user})

class Settings(View):
    """
    settings
    """
    template_name = 'settings.html'
    @method_decorator(login_required)
    def get(self,request):
        return render(request, 'accounts/settings.html')

    @method_decorator(login_required)
    def post(self, request):
        user_id = request.user.uid
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        result = MyUser.objects.update_password(uid = user_id,current_password=current_password, password=new_password)

        if result == 'success':
            return render(request, 'accounts/success.html')
        else:
            return render(request, 'accounts/settings.html',{'error':result})

class SetProfile(View):
    """
    manage user profile
    """
    @method_decorator(login_required)
    def get(self, request):
        # uid = request.session['member_id']
        try:
            profile = UserProfile.objects.get(pid = request.user.uid)
        except UserProfile.DoesNotExist:
            return render(request, 'accounts/profile.html')
        else:
            return render(request, 'accounts/profile.html', {'profile':profile})
    
    @method_decorator(login_required)
    def post(self,request):
        uid = request.user.uid
        email = request.POST['email']
        name = request.POST['name']
        validation_email = request.POST['validation_email']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        university = request.POST['uni']
        subject = request.POST['subject']
        commencement = request.POST['commencement']
        about_oneself = request.POST['about_oneself']
        result = UserProfile.objects.profileManage(uid, email, name, validation_email,
            birthday, gender, university, subject,commencement,about_oneself,)
        if result == 'success':
            return render(request, 'accounts/success.html')
        else:
            return render(request, 'accounts/profile.html')


def isEmailAddressValid( email ):
    """
    validate email address
    """
    try:
        EmailField().clean(email)
        return True
    except ValidationError:
        return False



