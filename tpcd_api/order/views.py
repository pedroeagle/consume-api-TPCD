from item.serializers import ItemSerializer
from item.models import Item
from customer.models import Customer
from rest_framework.views import APIView
from order.models import Order
from .serializers import OrderSerializer, OrderDetailsSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from customer.serializers import CustomerNameSerializer, CustomerSerializer

class OrderView(APIView):
    def get(self, request, order):
        foundOrder = Order.objects.filter(o_orderkey=order).first()
        if foundOrder is None:
           raise NotFound(f'{order} order doesn\'t exist')
        order = OrderDetailsSerializer(foundOrder).data
        foundClient = Customer.objects.filter(c_custkey=order['o_custkey']).first()
        client = CustomerSerializer(foundClient).data
        foundItems = Item.objects.filter(l_orderkey=order['o_orderkey']).all()
        items = ItemSerializer(foundItems, many=True).data
        response = {
            'order': order,
            'customer': client,
            'items': items
        }
        return Response(response)
class OrderListView(APIView):
    def get(self, request):
        orders = OrderSerializer(Order.objects.all()[:10], many=True).data
        response = [{'order': order, 'customer': CustomerNameSerializer(Customer.objects.filter(c_custkey=order['o_custkey']).first()).data} for order in orders]
        return Response(response)