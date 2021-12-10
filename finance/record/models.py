from django.db import models
from django.contrib.auth.models import User
import datetime




class Expenditure(models.Model):
    purpose = models.CharField(max_length=1000, default="")
    amount = models.IntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.purpose


   
