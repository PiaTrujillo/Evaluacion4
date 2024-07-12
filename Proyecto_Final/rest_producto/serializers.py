from rest_framework import serializers
from core.models import Producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields =['sku','dv','nombre','primer_apellido','segundo_apellido','descripcion','categoria','precio']