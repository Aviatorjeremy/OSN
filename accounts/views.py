from django.shortcuts import render
from django.forms import EmailField
from django.core.exceptions import ValidationError

from accounts.models import MyUser, UserProfile

def registration(request):
    """
    registration
    """
    if request.method == 'GET':
        return render(request, 'accounts/regist.html',{'session':request.session['member_id']})
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        udomain = request.POST['udomain']
        if password and isEmailAddressValid(email):
            result = MyUser.objects.create_user(email, password, udomain)
        else:
            return render(request, 'accounts/regist.html')
        return render(request, 'accounts/success.html')

def login(request):
    """
    lgoin
    """
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

    elif request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        user = MyUser.objects.get(email=email)

        if user.check_password(password):
            request.session['member_id']=user.uid
            return render(request, 'accounts/success.html',{'session':request.session['member_id']})
        else:
            return render(request, 'accounts/login.html')


def settings(request):
    """
    settings
    """
    if request.method == 'GET':
        return render(request, 'accounts/settings.html')

    elif request.method == 'POST':
        user_id = request.session['member_id']
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        result = MyUser.objects.update_password(uid = user_id,current_password=current_password, password=new_password)

        if result == 'success':
            return render(request, 'accounts/success.html')
        else:
            return render(request, 'accounts/settings.html',{'error':result})

def profileManage(request):
    """
    profile_setting
       datetime format is yyyy-mm-dd
    """
    user_id = request.session['member_id']

    if request.method == 'GET':
        try:
            result = UserProfile.objects.get(pid = user_id )
        except UserProfile.DoesNotExist:
            return render(request, 'accounts/profile.html')
        else:   
            return render(request, 'accounts/profile.html', {'result':result})

    elif request.method == 'POST':

        email = request.POST['email']
        name = request.POST['name']
        validation_email = request.POST['validation_email']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        uni = request.POST['uni']
        subject=request.POST['subject']
        commencement=request.POST['commencement']
        about_oneself = request.POST['about_oneself']

        result = UserProfile.objects.profileManage(user_id,email,name, validation_email,birthday,gender,uni,subject,commencement,about_oneself)
        if result == 'success':
            return render(request, 'accounts/success.html')
        else:
            return render(request, 'accounts/profile.html',{'error':result})


def isEmailAddressValid( email ):
    """
    validate email address
    """
    try:
        EmailField().clean(email)
        return True
    except ValidationError:
        return False



