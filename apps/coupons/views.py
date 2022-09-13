from django.db.models import Q

from rest_framework import generics
from rest_framework.filters import SearchFilter

from apps.coupons.models import Coupon, CouponIssueList
from apps.coupons.serializers import CouponCreateSerializer, CouponIssueSerializer


class CouponListRegisterView(generics.ListCreateAPIView):
    '''
    쿠폰 발급 내역 조회 및 필터링 API + 발급쿠폰 등록 API
    기능설명 : 
        필터링1(쿠폰 사용 여부) :  /?search=1(사용완료), /?search=0(미사용)
        필터링2(쿠폰 타입별 ) : /?q=1(50%할인쿠폰), /?q=2(배송비무료쿠폰), /?q=3(1000원 할인쿠폰)
        필터링3(필터링1+2 동시사용) : 사용완료이면서 배송비무료쿠폰, 사용완료이면서 1000원할인쿠폰 등 조합 가능, 예) /?search=1&q=2
        발급 쿠폰 등록 : /api/coupon/new/ 에서 발급된 쿠폰번호를 입력하면 선정된 유저에 등록
    에러처리 : 발급쿠폰 등록시 사용된 쿠폰이면 "쿠폰번호가 이미 사용되었습니다." 에러메시지 반환
    '''
    serializer_class = CouponIssueSerializer
    
    filter_backends = [SearchFilter]
    search_fields = ('is_use', )

    # 필터링 조합을 위해 get_queryset 오버라이딩하여 커스텀 진행
    def get_queryset(self, *args, **kwargs):
        queryset_list = CouponIssueList.objects.all().select_related("user", "coupon", "coupon__coupon_type")
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(coupon__coupon_type__id__icontains=query) 
            ).distinct()
        return queryset_list


class CouponCreateView(generics.CreateAPIView):
    '''
    신규 쿠폰 생성 API
    기능설명 : 신규 쿠폰번호와 쿠폰타입을 지정하면 신규쿠폰 생성
    에러처리 : 쿠폰번호 중복시 "쿠폰번호가 중복입니다. 쿠폰번호를 확인해주세요." 에러메세지 반환
    '''
    queryset = Coupon.objects.all()
    serializer_class = CouponCreateSerializer