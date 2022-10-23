from django.db import models


# Create your models here.
class Unit(models.Model):
    dimension_width = models.FloatField()
    dimension_length = models.FloatField(default=3)
    dimension_height = models.FloatField(default=3)
    unit_number = models.IntegerField(unique=True)
    available = models.BooleanField()

    def __str__(self):
        return f'Unit number: {self.unit_number}: Dimensions {self.dimension_width}, {self.dimension_length}, ' \
               f'{self.dimension_height} (width/length/height). Availability: {self.available}'


class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    business_name = models.CharField(blank=True, max_length=40)
    email_address = models.CharField(blank=True, max_length=50)
    phone_number = models.TextField(
        blank=True)  # TODO: add phone number validation (https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models)
    street_address = models.CharField(blank=True, max_length=50)  # TODO: Add length validation
    unit_access = models.ManyToManyField(Unit, related_name='customers', blank=True)

    def __str__(self):
        return f'Customer name: {self.first_name} {self.last_name}. \n Email: {self.email_address}\n Phone:{self.phone_number}\n' \
               f' Access to unit: {self.unit_access}'


class Transaction(models.Model):
    date = models.DateTimeField()
    unit_number = models.OneToOneField(Unit, on_delete=models.CASCADE)
    payment_destination = models.CharField(max_length=20)
