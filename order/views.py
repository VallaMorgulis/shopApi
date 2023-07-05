from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from order.serializers import OrderSerializer


class CreateOrderView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        user = request.user
        orders = user.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)