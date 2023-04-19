from django.db import models


# Create your models here.
class student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        db_table = "student"

