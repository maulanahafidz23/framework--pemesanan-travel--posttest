from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from luxe.models import Customers, TourPackage, Booking
import random

fake = Faker('id_ID')

class Command(BaseCommand):
    help = 'Seed data for Customers, TourPackage, and Booking models using Faker'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Seed Customers
        for _ in range(10):
            Customers.objects.create(
                nik=fake.unique.random_number(digits=16),
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
            )

        # Seed TourPackages
        rute = [
             ("Samarinda", "Balikpapan"),
            ("Balikpapan", "Samarinda"),
            ("Samarinda", "Tenggarong"),
            ("Tenggarong", "Samarinda"),
            ("Samarinda", "Bontang"),
            ("Bontang", "Samarinda"),
            ("Samarinda", "Sangatta"),
            ("Sangatta", "Samarinda"),
            ("Samarinda", "Berau"),
            ("Berau", "Samarinda"),
            ("Samarinda", "Tanjung Selor"),
            ("Tanjung Selor", "Samarinda"),
            ("Balikpapan", "IKN"),
            ("IKN", "Balikpapan"),
            ("Samarinda", "Banjarmasin"),
            ("Banjarmasin", "Samarinda"),
        ]
        
        for start, end in rute:
            TourPackage.objects.create(
                name=f"{start} to {end}",
                price=random.uniform(1000000, 5000000),
                start_location=start,
                end_location=end,
                transportation_type=random.choice(["Mini Bus", "Van"]),
            )

        # Seed Bookings
        customers = list(Customers.objects.all())  
        tour_packages = list(TourPackage.objects.all())  
        for _ in range(10):
            customer = random.choice(customers)
            tour_package = random.choice(tour_packages)
            travel_date = fake.future_date(end_date="+1y")
            number_of_travelers = random.randint(1, 5)
            
            Booking.objects.create(
                customers=customer,
                tour_package=tour_package,
                booking_date=fake.date_time_between(start_date="-1y", end_date="now", tzinfo=timezone.get_current_timezone()),
                travel_date=travel_date,
                number_of_travelers=number_of_travelers,
                total_price=tour_package.price * number_of_travelers,
                payment_status=random.choice(['PENDING', 'PAID', 'CANCELLED']),
                special_requests=fake.sentence() if random.choice([True, False]) else None
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded data'))