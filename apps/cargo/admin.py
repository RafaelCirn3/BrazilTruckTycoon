from django.contrib import admin
from .models import CargoModel
# Register your models here.


@admin.register(CargoModel)
class CargoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'weight', 'volume', 'value', 'destination', 'delivery_date')
    search_fields = ('name', 'description', 'destination')
    list_filter = ('delivery_date',)
    ordering = ('-delivery_date',)
    list_per_page = 20

