"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.cargo.api.viewsets import CargoViewSet
from apps.drivers.api.viewsets import DriverViewSet
from apps.trucks.api.viewsets import TruckViewSet
from apps.gameroutes.api.viewsets import GameRoutesViewSet
from apps.mechanics.api.viewsets import PartsViewSet, WearOfPartsViewSet, PartsMaintenanceViewSet, PartsTypeViewSet
# Create a router and register our viewset with it.
router = DefaultRouter()
#gameroutes
router.register(r'game_routes', GameRoutesViewSet, basename='game_routes')
#trucks
router.register(r'trucks', TruckViewSet, basename='trucks')
#cargo
router.register(r'cargo', CargoViewSet, basename='cargo')
#drivers
router.register(r'driver', DriverViewSet,basename='driver')
#mechanics
router.register(r'parts', PartsViewSet, basename='parts')
router.register(r'wear_of_parts', WearOfPartsViewSet, basename='wear_of_parts')
router.register(r'parts_maintenance', PartsMaintenanceViewSet, basename='parts_maintenance')
router.register(r'parts_type', PartsTypeViewSet, basename='parts_type')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
