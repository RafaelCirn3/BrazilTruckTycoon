from rest_framework import viewsets
from .serializers import CargoSerializer
from ..models import CargoModel
from rest_framework.permissions import IsAuthenticated

class CargoViewSet(viewsets.ModelViewSet):
    queryset = CargoModel.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']