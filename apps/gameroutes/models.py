from django.db import models

class GameRoutes(models.Model):
    name = models.CharField(max_length=100)
    distance = models.FloatField()
    dificulty = models.CharField(max_length=100)
    road_condition = models.CharField(max_length=100)
    def __str__(self):
        return self.name