from django.db import models


# Create your models here.i
class Data(models.Model):
    name = models.CharField(max_length=20)
    ages = models.IntegerField()
    sex = models.CharField(max_length=10)





