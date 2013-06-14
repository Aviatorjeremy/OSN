from django.shortcuts import render
from django.forms import EmailField
from django.core.exceptions import ValidationError
from django.views.generic.base import View
from django.contrib.auth import logout

from accounts.models import MyUser, UserProfile

class Registration(View):
    """
    registration
    """
    def get(self,request):
        return render(request, 'accounts/regist.html',{'session':request.session['member_id']})
    
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
        return render(request, 'accounts/login.html')

    def post(self, request):

        email = request.POST['email']
        password = request.POST['password']
        user = MyUser.objects.get(email=email)

        if user.check_password(password):
            request.session['member_id']=user.uid
            return render(request, 'accounts/success.html',{'session':request.session['member_id']})
        else:
            return render(request, 'accounts/login.html')

class Logout(View):
    """
    Logout
    """
    def get(self, request):
        logout(request)
        return render(request, 'accounts/success.html',{'session':request.session['member_id']})

class Settings(View):
    """
    settings
    """
    def get(self,request):
        return render(request, 'accounts/settings.html')

    def post(self, request):
        user_id = request.session['member_id']
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
    
    def get(self, request):
        uid = request.session['member_id']
        try:
            profile = UserProfile.objects.get(pid = uid)
        except UserProfile.DoesNotExist:
            return render(request, 'accounts/profile.html')
        else:
            return render(request, 'accounts/profile.html', {'profile':profile})
    
    def post(self,request):
        uid = request.session['member_id']
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



