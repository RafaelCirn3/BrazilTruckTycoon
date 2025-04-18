from ..models import Truck
from rest_framework import viewsets
from .serializers import TruckSerializer

class TruckViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trucks to be viewed or edited.
    """
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    http_method_names = ['get', 'post', 'put', 'delete']