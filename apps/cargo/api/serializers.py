from rest_framework.serializers import ModelSerializer
from ..models import CargoModel

class CargoSerializer(ModelSerializer):
    class Meta:
        model = CargoModel
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'value': {'required': True},
            'destination': {'required': True},
            'delivery_date': {'required': True}
        }