from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class personal_details(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    dob = models.DateField()
    w = models.IntegerField()
    h = models.IntegerField()
    disease = models.CharField(max_length = 20)


class goals(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    gname = models.CharField(max_length=20)
    gdesc = models.TextField()
    sdate = models.DateField()
    tdate = models.DateField()
    gtag = models.CharField(max_length=20)
    gstatus = models.CharField(max_length=20)


class exercise_tracker(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    ename = models.CharField(max_length=50)
    edesc = models.TextField()
    etag = models.CharField(max_length=20)
    created_at = models.DateField()
    priority = models.IntegerField()
    log = models.TextField(default="")

class blog(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    date_published = models.DateField()
    tag = models.CharField(max_length=20)
    intro = models.TextField()
    content = models.TextField()