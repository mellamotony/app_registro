"""
URL configuration for app_registro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from registro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('singup/', views.singup, name= 'singup'),
    path('singin/', views.singin, name='singin'),
    path('singout/', views.singout, name='singout'),
    path('producto/', views.recibir_producto, name='recibir producto'),
    path('recivirp/', views.productos_view, name='mandar producto'),
    path('cliente/', views.cliente, name='cliente'),
    path('recivir_cliente/', views.cliente_view, name='mostrar Cliente'),
    path('actualizarp/<int:id>/', views.actualizar_producto, name='actualizar producto'),
    path('actualizarc/<int:id>/', views.actualizar_cliente, name='actualizar cliente'),
    path('pedido/', views.recibir_pedido, name='recibir pedido'),
    path('obtenerpedido/', views.obtener_pedidos, name='obtener pedido'),
    
]