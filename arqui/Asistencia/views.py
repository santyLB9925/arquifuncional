from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Asistencia.models import Asistencia
from Asistencia.serializer import AsistenciaSerializers

class AsistenciaList(APIView):
    # METODO GET PARA SOLICITAR INFO
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Asistencia.objects.filter(delete = False)
        #many = True Si aplica si retorno multiples objetos
        serializer = AsistenciaSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AsistenciaSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class  AsistenciaDetail(APIView):
    def get_object(self, id):
        try:
            return Asistencia.objects.get(pk=id, delete=False)
        except Asistencia.DoesNotExist:
            return 404
    
    def get(self, request, id, format=None):
        Asistencia = self.get_object(id)
        if Asistencia != 404:
            #many = True No aplica si retorno un solo objeto
            serializer = AsistenciaSerializers(Asistencia)
            return Response(serializer.data)
        else:
            return Response(Asistencia)
    
    def put(self, request, id, format=None):
        Asistencia = self.get_object(id)
        if Asistencia != 404:
            serializer = AsistenciaSerializers(Asistencia, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)




# Create your views here.

