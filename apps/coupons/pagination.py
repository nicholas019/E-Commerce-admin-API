from rest_framework.pagination import PageNumberPagination

class CouponPageNumberPagination(PageNumberPagination):
    page_size = 20