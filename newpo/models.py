import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

from django.db import models,DatabaseError

class NewPo(models.Model):
	