from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    summary = models.TextField(default='This is awesome!!')
    feature = models.BooleanField(default=True)  # when empty null = True , default = True
    # password = models.CharField(max_length=50)
