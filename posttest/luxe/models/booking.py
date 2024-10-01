from django.db import models
from luxe.models.customers import Customers
from luxe.models.package import TourPackage

class Booking(models.Model):
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    travel_date = models.DateField()
    number_of_travelers = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    payment_status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('CANCELLED', 'Cancelled')
    ])
    special_requests = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Hitung total_price berdasarkan tour_package dan number_of_travelers
        if self.tour_package and self.number_of_travelers:
            self.total_price = self.tour_package.price * self.number_of_travelers
        else:
            self.total_price = 0  # Set ke 0 jika tidak ada tour_package atau traveler
        super().save(*args, **kwargs)  
        
        from luxe.models import Receipt
        # Buat Receipt baru setelah Booking disimpan
        Receipt.objects.get_or_create(
            booking=self,
            defaults={'amount': self.total_price, 'status': 'DRAFT'}
        )

    def __str__(self):
        return f"{self.customers.name} - {self.number_of_travelers} - {self.tour_package.name} - {self.travel_date}"
