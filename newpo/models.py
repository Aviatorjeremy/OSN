from django.db import models
from accounts.models import MyUser as User

class Message(models.Model):
    CONTENT_TYPE = (
        (u'T', u'TWEET'),
        (u'P', u'PHOTO'),
        (u'B', u'BLOG'),
    )
    mid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    time_published = models.DateTimeField()
    tweet = models.CharField(max_length=140)
    content_type = models.CharField(max_length=500, choices=CONTENT_TYPE)
    source_loc = models.FilePathField(blank=True,null=True)
    like_num = models.IntegerField(default=0)
    share_num = models.IntegerField(default=0)

class Comment(models.Model):
    cid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    message = models.ForeignKey(Message)
    ctxt = models.CharField(max_length=140)