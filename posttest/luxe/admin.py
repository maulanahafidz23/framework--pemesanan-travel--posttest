from django.contrib import admin
from .models import Customers
from .models import TourPackage
from .models import Booking
from .models import Receipt

#Receipt
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customers', 'tour_package', 'payment_status', 'total_price', 'travel_date')

    # Override untuk membuat resi
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Jika status pembayaran PAID
        if obj.payment_status == 'PAID':
            # Cek apakah resi sudah ada
            if not hasattr(obj, 'receipt'):
                # Jika resi belum ada, buat resi baru
                Receipt.objects.create(
                    booking=obj,
                    amount=obj.total_price,
                    status='FINAL'
                )
            else:
                obj.receipt.amount = obj.total_price
                obj.receipt.status = 'FINAL'
                obj.receipt.save()
        else:
            # Jika status pembayaran bukan PAID
            if not hasattr(obj, 'receipt'):
                Receipt.objects.create(
                    booking=obj,
                    amount=obj.total_price,
                    status='DRAFT'
                )
            else:
                obj.receipt.amount = obj.total_price
                obj.receipt.status = 'DRAFT'
                obj.receipt.save()

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'status', 'created_at')
    readonly_fields = ('amount',)  

# Register your models here.
admin.site.register(Customers)
admin.site.register(TourPackage)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Booking, BookingAdmin)
