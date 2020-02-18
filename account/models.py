from django.db import models


class Profile(models.Model):
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    studno = models.CharField( max_length=15)
    section = models.IntegerField()



