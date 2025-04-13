from django.db import models

# Create your models here.
class CargoModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Cargo Name')
    description = models.TextField(verbose_name='Description')
    weight = models.FloatField(verbose_name='Weight (kg)', blank=True, null=True)
    volume = models.FloatField(verbose_name='Volume (m³)', blank=True, null=True)
    value = models.FloatField(verbose_name='Value ($)')
    destination = models.CharField(max_length=255, verbose_name='Destination')
    delivery_date = models.DateField(verbose_name='Delivery Date')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        ordering = ['delivery_date']
