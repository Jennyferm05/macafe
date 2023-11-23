from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrar_venta/', views.registrar_venta, name='registrar_venta'),
    path('ventas/', views.ventas, name='ventas')

]
