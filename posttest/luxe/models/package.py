from django.db import models

class TourPackage(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    transportation_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.price} "