from django.urls import path

from apps.coupons.views import CouponListRegisterView, CouponCreateView

urlpatterns = [
    path("", CouponListRegisterView.as_view()),
    path("new/", CouponCreateView.as_view()),
    
]