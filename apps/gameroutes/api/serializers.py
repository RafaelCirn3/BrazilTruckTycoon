from rest_framework import serializers
from ..models import GameRoutes

class GameRoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRoutes
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'required': True},
            'distance': {'required': True},
            'dificulty': {'required': True},
            'road_condition': {'required': True}
        }