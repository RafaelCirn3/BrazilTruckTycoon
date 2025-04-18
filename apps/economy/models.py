from django.db import models

class fuelPrice(models.Model):
    """
    Model representing the fuel price.
    """
    fuel_type = models.CharField(max_length=50, unique=True)
    price_per_litre = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.fuel_type}: {self.price_per_litre}"

class cargoPrices(models.Model):
    """
    Model representing the cargo prices.
    """
    cargo_type = models.CharField(max_length=50, unique=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cargo_type}: {self.price_per_kg}"

class partPrices(models.Model):
    """
    Model representing the part prices.
    """
    part_name = models.CharField(max_length=50, unique=True)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.part_name}: {self.price_per_unit}"


