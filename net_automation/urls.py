from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('devices', views.devices, name="devices"),
    path('configure', views.configure, name="configure"),
    path('verify_config', views.verify_config, name="verify_config"),
    path('log', views.log, name="log")
]
