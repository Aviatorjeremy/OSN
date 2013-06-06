from django.db import models
#git test
class Person(models.Model):
    """
    The information of a user includes the nick name, real name, birthday, gender, university, subject, commencement date, and introduction about oneself.
    """
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    login_email = models.EmailField(max_length=50)
    validation_email = models.EmailField(max_length=50)
    birhday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)
    university = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    commencement = models.DateField()
    about_oneself = models.TextField(max_length=500)

class Content():
    """
    Contents including tweets, images and so on.
    """
    time = models.TimeField(primary_key=True)
    tweet = models.CharField(max_length=140)
    image = models.ImageField(blank=True)