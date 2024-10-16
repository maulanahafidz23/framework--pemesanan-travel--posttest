from django.shortcuts import render, redirect, get_object_or_404
from .models import Customers
from .forms import CustomersForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def contact(request):
    return render(request, 'homepage/contact.html')

def booking(request):
    return render(request, 'homepage/booking.html')

# READ Customer


def customer_index(request):
    query = request.GET.get('q')
    customers = Customers.objects.all()
    if query:
        customers = Customers.objects.filter(
            Q(name__icontains=query) |
            Q(nik__icontains=query) |
            Q(email__icontains=query) |
            Q(phone_number__icontains=query)
        )
    else:
        customers = Customers.objects.all()
    return render(request, 'customer/index.html', {'customers': customers, 'query': query})

# CREATE Customer
def customer_create(request):
    if request.method == 'POST':
        form = CustomersForm(request.POST)
        if form.is_valid():
            form.save() # Simpan data customer ke database
            messages.success(request, 'Customer berhasil dibuat!') # Pesan sukses
            return redirect('customer_index') # Redirect ke halaman index customer
    else:
        form = CustomersForm()
    return render(request, 'customer/create.html', {'form': form})

# UPDATE Customer
def customer_update(request, customer_id):
    customer = get_object_or_404(Customers, id=customer_id)
    if request.method == 'POST':
        form = CustomersForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data customer berhasil diubah!')
            return redirect('customer_index')
    else:
        form = CustomersForm(instance=customer)
        return render(request, 'customer/update.html', {'form': form, 'customer': customer})

# DELETE Customer
def customer_delete(request, customer_id):
    customer = get_object_or_404(Customers, id=customer_id)
    customer.delete()
    messages.success(request, 'Data customer berhasil dihapus')
    return JsonResponse({'success': True})
    
