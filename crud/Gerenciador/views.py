from rest_framework import viewsets
from .models import Pessoa
from .serializers import ItemSerializer

class PessoaView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Pessoa.objects.all()
