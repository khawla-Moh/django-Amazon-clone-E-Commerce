from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Product,Brand,Reviews,ProductImages
from . import serializers
from .pagination import ApiPagination





class ProductListAPI(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=serializers.ProductListSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['brand', 'flag']
    search_fields = ['name', 'description','subtitle']
    ordering_fields = ['price']


class ProductDetailAPI(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=serializers.ProductDetailSerializer    



class BrandListAPI(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=serializers.BrandListSerializer    
    pagination_class=ApiPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    

class BrandDetailAPI(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=serializers.BrandDetailSerializer    