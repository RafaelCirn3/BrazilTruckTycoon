from ..models import partPrices, fuelPrice, cargoPrices
from rest_framework import serializers

class FuelPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = fuelPrice
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'price_per_litre': {'required': True},
            'fuel_type': {'required': True},
            
        }

class CargoPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = cargoPrices
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'cargo_type': {'required': True},
            'price_per_kg': {'required': True},
        }

class PartPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = partPrices
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'part_name': {'required': True},
            'price_per_unit': {'required': True},
        }