from django.db import models

class parts(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class parts_type(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class wear_of_parts(models.Model):
    part = models.ForeignKey(parts, on_delete=models.CASCADE)
    wear_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    last_replacement_date = models.DateField()

    def __str__(self):
        return f"{self.part.name} - {self.wear_percentage}%"
    
class parts_maintenance(models.Model):
    part = models.ForeignKey(parts, on_delete=models.CASCADE)
    maintenance_date = models.DateField()
    maintenance_type = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return f"{self.part.name} - {self.maintenance_type} on {self.maintenance_date}"