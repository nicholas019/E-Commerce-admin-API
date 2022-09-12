from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.orders.models import WantedData

from apps.orders.serializers import OrderSerializer


class OrderListView(generics.ListAPIView):
    '''
    주문에 대한 내역 조회API
    주요기능 : 주문 리스트 조회, 주문리스트 검색(주문자명, 주문자ID, 주문상태, 주문시간, 배송상태), 주문리스트 정렬(주문시간별, 주문상태별)
    '''
    queryset = WantedData.objects.select_related('buyer', 'delivery_state').all()\
        .prefetch_related('buyer__delivery_info','buyer__delivery_info__country_code')
    # selcet_related와 prefetch를 활용해 쿼리 최적화 진행
    serializer_class = OrderSerializer

    filter_backends = [SearchFilter, OrderingFilter]

    ordering_fields = ('date', 'delivery_state__name' )
    search_fields = (
        'delivery_state__name', 
        'buyer__name',
        'buyer__nickname',
        'pay_state',
        'date' )