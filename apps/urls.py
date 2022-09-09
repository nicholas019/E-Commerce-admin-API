from django.urls import path, include

urlpatterns = [
    path("user/", include('apps.users.urls')),    
    path("order/", include('apps.orders.urls')),    
    path("coupon/", include('apps.coupons.urls')),    
]