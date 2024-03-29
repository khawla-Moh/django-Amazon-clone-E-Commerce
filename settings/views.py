from django.shortcuts import render
from django.db.models.aggregates import Count
from products.models import Product,Brand,Reviews



# Create your views here.
def home(request):
    new_product=Product.objects.filter(flag='new')[:10]
    sale_product=Product.objects.filter(flag='sale')[:10]
    feature_product=Product.objects.filter(flag='feature')[:10]
    brands=Brand.objects.annotate(product_count=Count('product_prand'))[:10]
    reviews=Reviews.objects.all





    return render(request,'settings/home.html',{
        'new_product':new_product,
        'sale_product':sale_product,
        'feature_product':feature_product,
        'brand':brands,
        'reviews':reviews
    })