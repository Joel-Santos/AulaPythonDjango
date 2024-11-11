# pedidos/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Pedido
from .serializers import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
