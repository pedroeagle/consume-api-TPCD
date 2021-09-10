from item.serializers import ItemSerializer
from item.models import Item
from client.models import Client
from rest_framework.views import APIView
from order.models import Order
from .serializers import OrderSerializer, OrderDetailsSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from client.serializers import ClientNameSerializer, ClientSerializer

class OrderView(APIView):
    def get(self, request, order):
        foundOrder = Order.objects.filter(o_orderkey=order).first()
        if foundOrder is None:
           raise NotFound(f'{order} order doesn\'t exist')
        order = OrderDetailsSerializer(foundOrder).data
        foundClient = Client.objects.filter(c_custkey=order['o_custkey']).first()
        client = ClientSerializer(foundClient).data
        foundItems = Item.objects.filter(l_orderkey=order['o_orderkey']).all()
        items = ItemSerializer(foundItems, many=True).data
        response = {
            'order': order,
            'client': client,
            'items': items
        }
        return Response(response)
class OrderListView(APIView):
    def get(self, request):
        orders = OrderSerializer(Order.objects.all()[:10], many=True).data
        response = [{'order': order, 'client': ClientNameSerializer(Client.objects.filter(c_custkey=order['o_custkey']).first()).data} for order in orders]
        return Response(response)