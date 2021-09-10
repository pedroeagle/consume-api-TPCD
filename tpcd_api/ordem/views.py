from django.shortcuts import render
from rest_framework.views import APIView
from ordem.models import Ordem
from .serializers import OrdemSerializer
from rest_framework.response import Response

class OrdemView(APIView):
    def get(self, request):
        ordens = Ordem.objects.all()[:2]
        print(len(ordens))
        serializer = OrdemSerializer(ordens, many=True)
        return Response(serializer.data)
