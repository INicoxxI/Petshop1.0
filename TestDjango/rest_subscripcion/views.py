from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csfr_exempt
from core.models import Subscripcion
from django.contrib.auth.models import User 
from .serializers import SubscripcionSerializer


@crsf_exempt
@api_view(['POST'])
def obtener_subscripcion(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        id_usuario = data['id_usuario']

        try
            user = User.objects.get(username=id_usuario)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try
            subscripcion = subscripcion.objects.get(usuario=user)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SubscripcionSerializer(subscripcion)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

@crsf_exempt
@api_view(['PUT'])
def desactivar_Subscripcion(request):

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        id_usuario = data['id_usuario']

        try
            user = User.objects.get(username=id_usuario)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        subscripcion = subscripcion.objects.get(usuario=user)
        subscripcion.vigente = False
        subscripcion.save()

@crsf_exempt
@api_view(['PUT'])
def activar_Subscripcion(request):

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        id_usuario = data['id_usuario']

        try
            user = User.objects.get(username=id_usuario)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        subscripcion = subscripcion.objects.get(usuario=user)
        subscripcion.vigente = True
        subscripcion.save()