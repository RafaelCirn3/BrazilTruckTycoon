from rest_framework import viewsets
from .serializers import DriverSerializer
from ..models import DriverModel
from rest_framework.permissions import IsAuthenticated

class DriverViewSet(viewsets.ModelViewSet):
    queryset = DriverModel.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get','post', 'put', 'patch', 'delete']