from django.db import models

# Create your models here.
class Unit(models.Model):
    dimension_width = models.FloatField()
    dimension_length = models.FloatField()
    dimension_height = models.FloatField(default=3)
    unit_number = models.IntegerField(unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return (f'Unidad {self.unit_number}:({self.dimension_width} x {self.dimension_length}): '
                f'{"Disponible" if self.available is True else "No disponible"}')

class Client(models.Model):
    MONTHLY = 'MONTH'
    ANNUAL = 'ANNUAL'
    QUARTERLY = 'QUARTERLY'
    SEMESTER = 'SEMESTERLY'
    CONTRACT_TYPES = [
        (MONTHLY, 'Monthly'),
        (ANNUAL, 'Annually'),
        (QUARTERLY, '3mos'),
        (SEMESTER, '6mos'),
    ]
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    business_name = models.CharField(blank=True, max_length=40)
    email_address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)  # TODO: add phone number validation (https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models)
    street_address = models.CharField(blank=True, max_length=50)  # TODO: Add length validation
    unit_access = models.ManyToManyField(Unit, related_name='units', default=None)
    monthly_charge = models.FloatField()
    contract_start_date = models.DateField()
    contract_type = models.CharField(choices=CONTRACT_TYPES, default=MONTHLY, max_length=40)
    last_date_paid = models.DateField()
    last_covered_date=models.DateField()
    documents = models.URLField(blank=True) #s3 bucket created for each customer with their contracts
    is_reporting_as_business = models.BooleanField(default=False)

    def __str__(self):

        unit_nums = []

        for unit in self.unit_access.all():
            unit_nums.append(unit.unit_number)
        unit_nums.sort()
        return f'{self.first_name} {self.last_name} - Unidad: {unit_nums}'


class Transaction(models.Model):
    BBVA = 'BBVA'
    AZTECA = 'Azteca - Ziomara'
    COSTCO = 'Costco Citibanamex - Layla'
    ORO = 'Oro Citibanamex - Layla'
    COSTCO_CITI_RAUL = 'Costco Citibanamex - Raul'
    SANTANDER_RAUL = 'Santander - Raul'
    PAYMENT_ACCOUNTS = [
        (BBVA, 'BBVA'),
        (AZTECA, 'Azteca - Ziomara'),
        (COSTCO, 'Costco Citibanamex - Layla'),
        (ORO, 'Oro Citibanamex - Layla'),
        (COSTCO_CITI_RAUL, 'Costco Citibanamex - Raul'),
        (SANTANDER_RAUL, 'Santander - Raul')
    ]
    client = models.OneToOneField(Client, related_name='client_name', blank=False, on_delete=models.CASCADE, default=None)
    amount = models.FloatField(default = 0.00)
    date = models.DateField()
    unit_number = models.OneToOneField(Unit, on_delete=models.CASCADE)
    payment_destination = models.CharField(max_length=30, choices=PAYMENT_ACCOUNTS)
