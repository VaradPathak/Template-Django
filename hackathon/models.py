from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=45)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
