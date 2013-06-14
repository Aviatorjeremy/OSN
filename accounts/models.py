import datetime
import re
import string
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8') 

from django.db import models,DatabaseError
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
        if user.check_password(current_password):
            user.set_password(password)
            user.save()
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
    def profileManage(self, uid, email, name, validation_email,
        birthday, gender, university, subject,commencement,about_oneself):
        """U$*#TRUIHRKJASRH"""
        try:
            profile = self.get(pid = uid)
        except UserProfile.DoesNotExist:
            profile = self.model(
                pid = MyUser.objects.get(uid=uid),
                email = UserProfileManager.normalize_email(email),
                name = str(name).translate(None, string.punctuation),
                validation_email= UserProfileManager.normalize_email(validation_email),
                birthday= birthday,
                gender=gender,
                university=str(university).translate(None, string.punctuation),
                subject=str(subject).translate(None, string.punctuation),
                commencement=commencement,
                about_oneself=str(about_oneself).translate(None, string.punctuation),
            )
            profile.save()
            return 'success'
        else:
            profile.email = UserProfileManager.normalize_email(email)
            profile.name = str(name).translate(None, string.punctuation)
            profile.birthday= birthday
            profile.gender=gender
            profile.university=str(university).translate(None, string.punctuation)
            profile.subject=str(subject).translate(None, string.punctuation)
            profile.commencement=commencement
            profile.about_oneself=str(about_oneself).translate(None, string.punctuation)
            profile.save()
            return 'success'

    # def update_profile(self, uid, email, name, birthday, gender, university, subject,commencement,about_oneself):
    # """
    # update profile (can be refactor **argm)
    # """
    #     if 
    #         profile = self.get(pid = uid)
    #         profile.email = UserProfileManager.normalize_email(email)
    #         profile.name = str(name).translate(None, string.punctuation)
    #         profile.birthday= birthday
    #         profile.gender=gender
    #         profile.university=str(university).translate(None, string.punctuation)
    #         profile.subject=str(subject).translate(None, string.punctuation)
    #         profile.commencement=commencement
    #         profile.about_oneself=str(about_oneself).translate(None, string.punctuation)
    #         profile.save()
        


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
    birthday = models.DateTimeField()
    gender = models.CharField(max_length=1, choices=GENDER)
    university = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    commencement = models.DateTimeField(blank=True)
    about_oneself = models.TextField(max_length=500)

    objects = UserProfileManager()

    def __unicode__(self):
        return self.name

class UniversityList(models.Model):
    uni_id = models.AutoField(primary_key=True)
    university_name = models.CharField(unique=True, max_length=50,)
    country = models.CharField(unique = True, max_length=50,)
