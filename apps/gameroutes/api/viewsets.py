from ..models import GameRoutes
from .serializers import GameRoutesSerializer
from rest_framework import viewsets

class GameRoutesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows game routes to be viewed or edited.
    """
    queryset = GameRoutes.objects.all()
    serializer_class = GameRoutesSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    