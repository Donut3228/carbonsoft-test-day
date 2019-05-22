from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register('sensor', views.SensorViewSet)
router.register('sensor-history', views.SensorHistoryViewSet)





urlpatterns = [
    path('', include(router.urls))
]