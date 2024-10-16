from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about),
    path('', views.homepage),
    path('contact', views.contact),
    path('booking', views.booking),
    path('customer', views.customer_index, name='customer_index'), # Read
    path('customer/create/', views.customer_create, name='customer_create'),# Create
    path('customer/update/<int:customer_id>/', views.customer_update, name='customer_update'), # Update
    path('customer/delete/<int:customer_id>', views.customer_delete, name='customer_delete'), # Delete
]