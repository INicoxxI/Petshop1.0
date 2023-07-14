from django.urls import path
from rest_subscripcion.views import obtener_subscripcion,desactivar_Subscripcion,activar_Subscripcion



urlpatterns = [
    path('obtener_subscripcion', obtener_subscripcion , name= "obtener_subscripcion")
    path('desactivar_subscripcion', desactivar_subscripcion , name= "desactivar_subscripcion")
    path('activar_Subscripcion', activar_Subscripcion , name= "activar_Subscripcion")

]