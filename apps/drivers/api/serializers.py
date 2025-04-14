from rest_framework.serializers import ModelSerializer
from ..models import DriverModel

class DriverSerializer(ModelSerializer):

    class Meta:
        model = DriverModel
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'name':{'required': True},
            'abilities':{'required': True},
            'weakness':{'required': True},
            'accident_historic':{'required': True}
        }