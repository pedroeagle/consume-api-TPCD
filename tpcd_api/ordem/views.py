from django.shortcuts import render
from rest_framework.views import APIView
from ordem.models import Ordem
from .serializers import OrdemSerializer
from rest_framework.response import Response

class OrdemView(APIView):
    def get(self, request):
        ordens = Ordem.objects.all()[:10]
        print(ordens)
        serializer = OrdemSerializer(data=ordens)
        serializer.is_valid()
        return Response(serializer.data)
