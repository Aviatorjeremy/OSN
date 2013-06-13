from django.shortcuts import render
from django.forms import EmailField
from django.core.exceptions import ValidationError

from accounts.models import MyUser

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

def isEmailAddressValid( email ):
    """
    validate email address
    """
    try:
        EmailField().clean(email)
        return True
    except ValidationError:
        return False



