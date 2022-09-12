from django.urls import path

from apps.orders.views import OrderListView, OrderDetailUpdateView
urlpatterns = [
    path("", OrderListView.as_view()),
    path("<int:pk>/", OrderDetailUpdateView.as_view()),
]