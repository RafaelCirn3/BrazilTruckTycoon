from django.db import models

class Trucks(models.Model):
    capacity = models.IntegerField()
    model = models.CharField(max_length=100)
    consume = models.IntegerField()
    condition = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    parts = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.brand} {self.model}"
    