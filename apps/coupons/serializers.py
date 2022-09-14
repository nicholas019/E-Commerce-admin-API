from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.users.models import User
from apps.coupons.models import Coupon, CouponIssueList, CouponType


class CouponTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponType
        fields = "__all__"

    def validate(self, validate_data): 
        '''
        신규 쿠폰 생성시 쿠폰번호 중복 방지 검사 기능
        기능 : type_name와 type_value가 동시에 중복이면 에러처리
        '''
        type_name  = validate_data['type_name']
        type_value = validate_data['type_value']

        if CouponType.objects.filter(type_name = type_name, type_value = type_value).exists(): 
            raise ValidationError("쿠폰 타입이 중복됩니다. 쿠폰타입을 확인해주세요.")        
        return validate_data


class CouponSerializer(serializers.ModelSerializer): 
    coupon_type = CouponTypeSerializer(read_only=True)
    
    class Meta: 
        model  = Coupon
        fields = [ 'pk', 'coupon_type', 'coupon_num' ]


class CouponCreateSerializer(serializers.ModelSerializer):
    '''
    신규 쿠폰 발급 시리얼라이저
    '''
    class Meta: 
        model  = Coupon
        fields = [ 'pk', 'coupon_type', 'coupon_num' ]
    
    def validate(self, validate_data): 
        '''
        신규 쿠폰 타입 생성시 쿠폰 종류 중복 방지 검사 기능
        '''
        coupon_num = validate_data['coupon_num']

        if Coupon.objects.filter(coupon_num = coupon_num).exists(): 
            raise ValidationError("쿠폰번호가 중복입니다. 쿠폰번호를 확인해주세요.")        
        return validate_data



class CouponIssueSerializer(serializers.ModelSerializer):
    '''
    발급된 쿠폰 등록 시리얼라이저
    '''
    coupon = CouponSerializer()

    class Meta:
        model  = CouponIssueList
        fields = [ "pk", "user", "coupon", "is_use" ]

    def validate(self, validate_data):
        '''
        신규 쿠폰 생성시 쿠폰번호 등록시 쿠폰 사용여부 검사 기능
        '''
        coupon_num = validate_data['coupon']['coupon_num']

        coupon = Coupon.objects.get(coupon_num = coupon_num)

        if CouponIssueList.objects.filter(coupon_id = coupon.id).exists(): 
            raise ValidationError("쿠폰번호가 이미 사용되었습니다.") 
        return validate_data

    def create(self, validate_data):
        nickname   = validate_data['user']
        coupon_num = validate_data['coupon']['coupon_num']
        
        user   = User.objects.get(nickname=nickname)
        coupon = Coupon.objects.get(coupon_num = coupon_num)

        return CouponIssueList.objects.create(
                user_id = user.id,
                coupon_id = coupon.id,
                is_use = False
                )
