from ..models import Trucks
from rest_framework import viewsets
from .serializers import TrucksSerializer

class TruckViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trucks to be viewed or edited.
    """
    queryset = Trucks.objects.all()
    serializer_class = TrucksSerializer
    http_method_names = ['get', 'post', 'put', 'delete']