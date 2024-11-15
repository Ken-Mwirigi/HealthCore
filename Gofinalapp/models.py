from django.db import models

# Create your models here.
class Members(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    yob = models.DateField()

    #method to save values with fullname
    def __str__(self):
        return self.fullname

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name