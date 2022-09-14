from django.urls import path

from apps.coupons.views import CouponListRegisterView, CouponListCreateView, CouponTypeCreateView

urlpatterns = [
    path("", CouponListRegisterView.as_view()),
    path("new/", CouponListCreateView.as_view()),
    path("type/", CouponTypeCreateView.as_view()),
]