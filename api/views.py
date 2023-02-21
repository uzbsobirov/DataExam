from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import *
from main.models import *
from rest_framework.response import Response
from rest_framework import status

class CategoriesApiView(APIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(data=serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
class CategoryApiView(APIView):
    serializer_class = CategorySerializer

    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        serializer = CategorySerializer(instance=category)
        return Response(data=serializer.data)
    
    def patch(self, request, slug):
        data = request.data
        category = get_object_or_404(Category, slug=slug)
        serializer = self.serializer_class(instance=category, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    
    def put(self, request, slug):
        data = request.data
        category = get_object_or_404(Category, slug=slug)
        serializer = self.serializer_class(instance=category, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        category.delete()
        return Response({"Deleted": "Category was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)

class ProductsApiView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = self.serializer_class(instance=products, many=True)
        return Response(data=serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)
    
class ProductApiView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=slug)
        serializer = ProductSerializer(instance=product)
        return Response(data=serializer.data)
    
    def patch(self, request, slug):
        data = request.data
        product = get_object_or_404(Product, slug=slug)
        serializer = self.serializer_class(instance=product, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    
    def put(self, request, slug):
        data = request.data
        product = get_object_or_404(Product, slug=slug)
        serializer = self.serializer_class(instance=product, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    
    def delete(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=slug)
        product.delete()
        return Response({"Deleted": "Product was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
    

class CustomersApiView(APIView):
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        serializer = self.serializer_class(instance=customers, many=True)
        return Response(data=serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)


class CustomerApiView(APIView):
    serializer_class = CustomerSerializer

    def get(self, request, email, *args, **kwargs):
        customer = get_object_or_404(Customer, email=email)
        serializer = CustomerSerializer(instance=customer)
        return Response(data=serializer.data)
    
    def patch(self, request, email):
        data = request.data
        customer = get_object_or_404(Customer, email=email)
        serializer = self.serializer_class(instance=customer, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    
    def put(self, request, email):
        data = request.data
        customer = get_object_or_404(Customer, email=email)
        serializer = self.serializer_class(instance=customer, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    
    def delete(self, request, email, *args, **kwargs):
        customer = get_object_or_404(Customer, email=email)
        customer.delete()
        return Response({"Deleted": "Customer was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
    

class InvertoriesApiView(APIView):
    serializer_class = InventorySerializer

    def get(self, request, *args, **kwargs):
        inventories = Inventory.objects.all()
        serializer = self.serializer_class(instance=inventories, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

class InventoryApiView(APIView):
    serializer_class = InventorySerializer

    def get(self, request, pk, *args, **kwargs):
        inventory = get_object_or_404(Inventory, pk=pk)
        serializer = self.serializer_class(instance=inventory)
        return Response(data=serializer.data)
    
    def patch(self, request, pk):
        data = request.data
        inventory = get_object_or_404(Inventory, pk=pk)
        serializer = self.serializer_class(instance=inventory, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    
    def put(self, request, pk):
        data = request.data
        inventory = get_object_or_404(Inventory, pk=pk)
        serializer = self.serializer_class(instance=inventory, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    
    def delete(self, request, pk, *args, **kwargs):
        inventory = get_object_or_404(Inventory, pk=pk)
        inventory.delete()
        return Response({"Deleted": "Inventory was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
    
class OrdersApiView(APIView):
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

class OrderApiView(APIView):
    serializer_class = OrderSerializer

    def get(self, request, pk, *args, **kwargs):
        order = get_object_or_404(Order, pk=pk)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data)
    
    def patch(self, request, pk):
        data = request.data
        order = get_object_or_404(Order, pk=pk)
        serializer = self.serializer_class(instance=order, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    
    def put(self, request, pk):
        data = request.data
        order = get_object_or_404(Order, pk=pk)
        serializer = self.serializer_class(instance=order, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    
    def delete(self, request, pk, *args, **kwargs):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return Response({"Deleted": "Order was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
    
class PPSApiView(APIView):
    serializer_class = ProductPhotoSerializer

    def get(self, request, *args, **kwargs):
        pps = ProductPhoto.objects.all()
        serializer = self.serializer_class(instance=pps, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)


class PPApiView(APIView):
    serializer_class = ProductPhotoSerializer

    def get(self, request, pk, *args, **kwargs):
        pp = get_object_or_404(ProductPhoto, pk=pk)
        serializer = self.serializer_class(instance=pp)
        return Response(data=serializer.data)
    
    def patch(self, request, pk):
        data = request.data
        pp = get_object_or_404(ProductPhoto, pk=pk)
        serializer = self.serializer_class(instance=pp, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    
    def put(self, request, pk):
        data = request.data
        pp = get_object_or_404(ProductPhoto, pk=pk)
        serializer = self.serializer_class(instance=pp, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    
    def delete(self, request, pk, *args, **kwargs):
        pp = get_object_or_404(ProductPhoto, pk=pk)
        pp.delete()
        return Response({"Deleted": "Product Photo was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)