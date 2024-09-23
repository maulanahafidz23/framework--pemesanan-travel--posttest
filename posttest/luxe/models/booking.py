from django.db import models
from luxe.models.customers import Customers
from luxe.models.package import TourPackage


class Booking(models.Model):
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    travel_date = models.DateField()
    number_of_travelers = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('CANCELLED', 'Cancelled')
    ])
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.traveler.name} - {self.tour_package.name}"