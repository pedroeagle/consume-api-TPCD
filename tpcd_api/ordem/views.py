from django.shortcuts import render
from rest_framework.views import APIView
from ordem.models import Ordem
from .serializers import OrdemSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class OrdemView(APIView):
    def get(self, request):
        ordens = Ordem.objects.all()[:10]
        serializer = OrdemSerializer(ordens, many=True)
        return Response(serializer.data)
    def get(self, request, ordem):
        foundOrder = Ordem.objects.filter(o_orderkey=ordem).first()
        if foundOrder is None:
           raise NotFound(f'{ordem} order doesn\'t exist')
        serializer = OrdemSerializer(foundOrder)
        return Response(serializer.data)
