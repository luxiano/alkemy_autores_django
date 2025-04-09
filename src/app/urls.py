from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('listado/', views.listado, name='listado'),
    path('listado_json/', views.listado_json, name='listado_json'),
    path('detalle_autor/<int:id>/', views.detalle_autor, name='detalle_autor'),
    path('borrar_autor/<int:id>/', views.borrar_autor, name='borrar_autor'),
    path('cambiar_estado/<int:id>/', views.cambiar_estado, name='cambiar_estado'),
    # Debe ser la última para que no choque con la anterior
    path('listado/<str:inactivo>/', views.listado, name='listado_inactivo'),
]