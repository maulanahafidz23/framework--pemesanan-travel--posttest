from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def contact(request):
    return render(request, 'homepage/contact.html')

def booking(request):
    return render(request, 'homepage/booking.html')