from rest_framework.serializers import ModelSerializer
from main.models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

        read_only_fields = ('date_created', 'date_updated', 'slug')

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

        read_only_fields = ('date_created', 'date_updated')

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

        read_only_fields = ('date_created', 'date_updated')

class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"

        read_only_fields = ('date_created', 'date_updated')

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

        read_only_fields = ('date_created', 'date_updated', 'total_price')

class ProductPhotoSerializer(ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = "__all__"

        read_only_fields = ('date_created', 'date_updated')