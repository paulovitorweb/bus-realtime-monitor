from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'terminal', views.TerminalViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('ws/', include(router.urls)),
    path('gps/', views.gps, name='gps')
]
