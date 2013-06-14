from django.db import models
from accounts.models import MyUser as User

class Message(models.Model):
    CONTENT_TYPE = (
        (u'T', u'TWEET'),
        (u'P', u'PHOTO'),
        (u'B', u'BLOG'),
    )
    mid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, db_column = 'user',)
    time_published = models.DateTimeField()
    tweet = models.CharField(max_length=140)
    content_type = models.CharField(max_length=500, choices=CONTENT_TYPE)
    source_loc = models.FilePathField(path=None)
    like_num = models.IntegerField(default=0)
    share_num = models.IntegerField(default=0)

<<<<<<< HEAD
    class meta:
    	ording = "-time_published"
=======
    def __unicode__(self):
        return tweet

    class Meta:
        ordering = ['-time_published']
>>>>>>> 647ccbabba625f42e5b644adcd0e092471a2b551

class Comment(models.Model):
    cid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, db_column = 'user')
    message = models.ForeignKey(Message, db_column = 'message')
    ctxt = models.CharField(max_length=140)

class MsgMeta(models.Model):
	mmid = models.AutoField(primary_key=True)
	mid = models.ForeignKey(Message, db_column = 'mid',)
	uid = models.ForeignKey(User, db_column = 'uid',)
	like = models.BooleanField(default=False)
	share = models.BooleanField(default=False)