from django.db import models

class ContactData(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=30)
    location = models.CharField(max_length=100)
    course = models.CharField(max_length=30)