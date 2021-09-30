from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import *
from Productos.views import *

router = DefaultRouter()
router.register('tipo', TipoApi)

urlpatterns = [
    path('crud/', include(router.urls))
]