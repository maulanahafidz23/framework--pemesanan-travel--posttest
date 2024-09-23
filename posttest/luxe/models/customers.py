from django.db import models

class Customers(models.Model):
    nik = models.CharField(max_length=16, unique=True)  
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name