from rest_framework import serializers

from apps.users.models import User
from apps.orders.models import CountryCode, DeliveryInfo


class ConutryCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryCode
        fields = [
            "pk",
            "code",
            "dcode",
            "name"
        ]


class DeliveryInfoSerializer(serializers.ModelSerializer):
    country_code = ConutryCodeSerializer(read_only=True)
    class Meta:
        model = DeliveryInfo
        fields = [
            'pk',
            "city",
            "zipx",
            'country_code'
            ]


class UserSerializer(serializers.ModelSerializer):
    delivery_info = DeliveryInfoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "pk", 
            "nickname", 
            "name", 
            "delivery_info"
            ]