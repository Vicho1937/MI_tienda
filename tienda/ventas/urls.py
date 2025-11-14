from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'ventas'

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet, basename='producto')

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('producto/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('producto/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('venta/registrar/', views.registrar_venta, name='registrar_venta'),
    path('ventas/lista/', views.lista_ventas, name='lista_ventas'),
    path('ventas/exportar/', views.exportar_ventas_csv, name='exportar_ventas'),
] + router.urls
