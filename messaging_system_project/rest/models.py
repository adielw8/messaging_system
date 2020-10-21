from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    message = models.CharField(max_length=500, default='Message (maximum 500 characters)')
    subject = models.CharField(max_length=30, default='Subject (maximum 30 characters)')
    creation_date = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)


