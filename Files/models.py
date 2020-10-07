from django.db import models


# Create your models here.
class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    belongsto = models.IntegerField(default=0)
    visibility = models.CharField(max_length=100, default="private")
    description = models.CharField(max_length=200, default="N/A")