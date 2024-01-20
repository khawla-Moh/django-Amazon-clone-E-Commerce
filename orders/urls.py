from django.urls import path
from .views import order_list,checkout,add_to_cart
from .api import OrderListAPI,OrderDetailAPI,ApplyCouponAPI,CreatetOrderAPI,CartCreateUpdateDelete



urlpatterns = [
    path('',order_list),
    path('checkout/',checkout),
    path('add_to_cart',add_to_cart),



    #______________api url_________________
    path('api/<str:username>/orders',OrderListAPI.as_view()),            #go to order for this user who orderd 
    path('api/<str:username>/<int:pk>/orders',OrderDetailAPI.as_view()) ,   #go to order for this user who orderd and product id
    path('api/<str:username>/<int:pk>/apply_coupon',ApplyCouponAPI.as_view()) ,  
    path('api/<str:username>/cart',CreatetOrderAPI.as_view()) ,  
    path('api/<str:username>/orders/create',CartCreateUpdateDelete.as_view()) ,  
    
    ]


