from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet
from . import views

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path("", lista_productos, name="lista_productos"),
    path("nuevo/", crear_producto, name="crear_producto"),
    path("editar/<int:id>/", editar_producto, name="editar_producto"),
    path("eliminar/<int:id>/", eliminar_producto, name="eliminar_producto"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("exportar/", views.exportar_excel, name="exportar_excel"),
    path("qr/<int:pk>/", views.qr_producto, name="qr_producto"),
    path("producto/<int:pk>/", views.detalle_producto, name="detalle_producto"),

]

urlpatterns += router.urls
