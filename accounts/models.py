import datetime
import re
import string
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class MyUserManager(BaseUserManager):
    def create_user(self, email, password, udomain):
        """
        Creates and saves a user with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            udomain=str(udomain).translate(None, string.punctuation)
        )
        user.set_password(password)
        user.save()
        return user

    def update_password(self, uid, current_password, password):
        """
        update_password
        """
        user = self.get(uid = uid)
        print user, password
        if user.check_password(current_password):
            user.set_password(password)
            user.save()
            print 'success'
            return 'success'
        else:
            return 'wrong password'



    def create_superuser(self, email, password, udomain):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email,
            password = password,
        )
        user.is_admin = True
        user.save()
        return user

class MyUser(AbstractBaseUser):
    """
    The information of a user(inc. name, email, validation_email, birthday, gender, university, subject, commencement datetime, and introduction about oneself.
    """
    uid = models.AutoField(primary_key=True)
    email = models.EmailField(
        max_length=50,
        unique=True,
        #db_index = True,
    )
    udomain = models.CharField(
        max_length=20,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)
    # name = models.models.CharField(max_length=20)
    # validation_email = models.EmailField(max_length=50)
    # birhday = models.DatetimeField()
    # gender = models.CharField(max_length=1, choices=GENDER)
    # university = models.CharField(max_length=40)
    # subject = models.CharField(max_length=40)
    # commencement = models.DatetimeField()
    # about_oneself = models.TextField(max_length=500)

    objects = MyUserManager()

    # def get_full_name(self):
    #   return self.name

    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return self.email

class UserProfileManager(BaseUserManager):
    def create_profile(self, email, name, validation_email,
        birthday, gender, university, subject,commencement,about_oneself):
        pass

class UserProfile(AbstractBaseUser):
    GENDER = (
        (u'M', u'Male'),
        (u'F', u'Female'),
        (u'O', u'Others'),
    )
    pid = models.OneToOneField(
        MyUser,
        primary_key=True,
        db_column = 'pid',
    )
    email = models.EmailField(
        max_length=50,
        unique=True,
        #db_index = True,
    )
    name = models.CharField(max_length=20)
    validation_email = models.EmailField(
        max_length=50,
        unique=True,
    )
    birhday = models.DateTimeField()
    gender = models.CharField(max_length=1, choices=GENDER)
    university = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    commencement = models.DateTimeField()
    about_oneself = models.TextField(max_length=500)

    