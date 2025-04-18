from ..models import Trucks
from rest_framework import serializers

class TrucksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trucks
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'capacity': {'required': True},
            'model': {'required': True},
            'consume': {'required': True},
            'condition': {'required': True},
            'brand': {'required': True},
            'parts': {'required': True}
        }