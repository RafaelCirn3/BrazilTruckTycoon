from ..models import partPrices, fuelPrice, cargoPrices
from .serializers import FuelPriceSerializer, CargoPricesSerializer, PartPricesSerializer
from rest_framework import viewsets 

class FuelPriceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows fuel prices to be viewed or edited.
    """
    queryset = fuelPrice.objects.all()
    serializer_class = FuelPriceSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class CargoPricesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cargo prices to be viewed or edited.
    """
    queryset = cargoPrices.objects.all()
    serializer_class = CargoPricesSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PartPricesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows part prices to be viewed or edited.
    """
    queryset = partPrices.objects.all()
    serializer_class = PartPricesSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
