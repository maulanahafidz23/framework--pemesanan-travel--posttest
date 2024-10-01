from django.db import models
from luxe.models import Booking

class Receipt(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('DRAFT', 'Draft'),
        ('FINAL', 'Final'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receipt for {self.booking} - {self.status}"
