from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now)
