from rest_framework import serializers
from .models import Pessoa
  
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'