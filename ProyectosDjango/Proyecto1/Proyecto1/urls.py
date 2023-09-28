"""
URL configuration for Proyecto1 project.

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
from Proyecto1.views import damefecha, saludo, despedida, calcularEdad, ruta1, ruta2, ruta3, diaActual, datosUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('despedida/', despedida),
    path('fecha/', damefecha),
    path('edades/<int:agno>', calcularEdad),
    
    # Ejercicio 2
    path('ruta1/', ruta1),
    path('ruta2/', ruta2),
    path('ruta3/', ruta3),
    
    path('dia/', diaActual),

    path('datos/<str:nombre>/<int:agno>/' ,datosUsuario)

]
