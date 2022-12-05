from django.db import models


class UserProfile(models.Model):
    firstname = models.CharField(max_length=51)
    lastname = models.CharField(max_length=51)
    address = models.CharField(max_length=101)
    useremail = models.EmailField(max_length=70, blank=True, unique=True)
    postal = models.IntegerField()
    weburl = models.CharField(max_length=101)
    password = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
