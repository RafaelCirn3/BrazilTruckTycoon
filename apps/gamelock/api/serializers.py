from rest_framework.serializers import ModelSerializer
from ..models import gamelock

class GameLockSerializer(ModelSerializer):
    """
    Serializer for the GameLock model.
    """
    class Meta:
        model = gamelock
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'game_time': {'required': True},
        }