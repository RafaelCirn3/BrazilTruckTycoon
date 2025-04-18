from rest_framework import serializers
from ..models import parts, parts_maintenance, parts_type, wear_of_parts

class PartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = parts
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'price': {'required': True},
            'quantity': {'required': True}
        }

class PartsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = parts_type
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True}
        }

class WearOfPartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = wear_of_parts
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'part': {'required': True},
            'wear_percentage': {'required': True},
            'last_replacement_date': {'required': True}
        }

class PartsMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = parts_maintenance
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'part': {'required': True},
            'maintenance_date': {'required': True},
            'maintenance_type': {'required': True},
            'notes': {'required': True}
        }