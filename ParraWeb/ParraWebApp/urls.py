from django.urls import path,include
from ParraWebApp import views
from register import views as reg

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('inicio',views.inicio,name="Inicio"),
    path('menu',views.menu,name="Menu"),
    path('insertar/',views.insert, name = "Insertar"),
    path('editartarea/<int:id>',views.editartarea, name="Editar"),
    path('terminartarea/<int:id>',views.terminartarea, name="Terminar"),
    path('eliminartarea/<int:id>',views.eliminartarea, name="Eliminar"),
    path('register/',reg.register,name="Registrar"),
    path('', include("django.contrib.auth.urls")), 
]