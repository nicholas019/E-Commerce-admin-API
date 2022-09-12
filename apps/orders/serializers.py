from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.orders.models import DeliveryState, WantedData
from apps.users.serializers import UserSerializer


class DeliveryStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryState
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    buyer          = UserSerializer(read_only = True)
    delivery_state = DeliveryStateSerializer()

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
        read_only_fields = ("price", "quantity", "pay_state")

    def validate(self, validated_data):
        '''
        배송상태 UPDATA를 위한 검사
        배송준비, 배송중, 배송완료, 주문취소 4개 이외의 데이터가 들어올시 에러처리
        '''
        if self.instance:
            data = validated_data['delivery_state']
            if not DeliveryState.objects.filter(name = data['name']).exists():
                raise ValidationError("잘못수정하였습니다. 배송준비, 배송중, 배송완료, 주문취소 중에 하나로 입력해주세요")
        return validated_data

    def update(self, instance, validated_data):
        data = validated_data['delivery_state']
        data = DeliveryState.objects.get(name = data['name'])
        instance.delivery_state = data
        
        instance.save()
        return instance
    