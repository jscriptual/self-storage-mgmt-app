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

