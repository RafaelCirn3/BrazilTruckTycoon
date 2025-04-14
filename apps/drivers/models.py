from django.db import models

class DriverModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Driver name')
    abilities = models.IntegerField(verbose_name='Abilities')
    weakness = models.IntegerField(verbose_name='Weakness')
    accident_historic =  models.IntegerField(verbose_name='Accident Historic')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Cargos'
        ordering =['name']
