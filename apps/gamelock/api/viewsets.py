from rest_framework import viewsets
from ..models import gamelock
from .serializers import GameLockSerializer

class GameLockViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows game locks to be viewed or edited.
    """
    queryset = gamelock.objects.all()
    serializer_class = GameLockSerializer
    http_method_names = ['get', 'post', 'put', 'delete']