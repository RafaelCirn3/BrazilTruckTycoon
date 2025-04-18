from rest_framework import viewsets
from ..models import wear_of_parts, parts, parts_maintenance, parts_type
from .serializers import WearOfPartsSerializer, PartsSerializer, PartsMaintenanceSerializer, PartsTypeSerializer

class WearOfPartsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows wear of parts to be viewed or edited.
    """
    queryset = wear_of_parts.objects.all()
    serializer_class = WearOfPartsSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PartsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parts to be viewed or edited.
    """
    queryset = parts.objects.all()
    serializer_class = PartsSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PartsMaintenanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parts maintenance to be viewed or edited.
    """
    queryset = parts_maintenance.objects.all()
    serializer_class = PartsMaintenanceSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PartsTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parts type to be viewed or edited.
    """
    queryset = parts_type.objects.all()
    serializer_class = PartsTypeSerializer
    http_method_names = ['get', 'post', 'put', 'delete']