from rest_framework import serializers

from apps.orders.models import WantedData
from apps.users.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    buyer          = UserSerializer(read_only = True)
    delivery_state = serializers.StringRelatedField()

    class Meta:
        model = WantedData
        fields = [
            "pk",
            "buyer", 
            "delivery_state", 
            "pay_state", 
            "quantity", 
            "price", 
            "date" 
            ]