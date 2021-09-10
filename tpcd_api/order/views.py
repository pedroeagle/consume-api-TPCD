from django.shortcuts import render
from rest_framework.views import APIView
from order.models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class OrderView(APIView):
    def get(self, request, order):
        foundOrder = Order.objects.filter(o_orderkey=order).first()
        if foundOrder is None:
           raise NotFound(f'{order} order doesn\'t exist')
        serializer = OrderSerializer(foundOrder)
        return Response(serializer.data)
class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()[:10]
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)