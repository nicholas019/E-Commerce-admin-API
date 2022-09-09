from django.db import models

from apps.users.models import User


class Coupon(models.Model):
    coupon_type = models.ForeignKey("CouponType", on_delete=models.CASCADE)
    coupon_num  = models.IntegerField()
    is_use      = models.BooleanField(default=False)

    class Meta:
        db_table = "coupons"


class CouponType(models.Model):
    type_name = models.CharField(max_length=45)

    class Meta:
        db_table = "coupon_types"


class CouponIssueList(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    counpon = models.ForeignKey("Coupon", on_delete=models.CASCADE)

    class Meta:
        db_table = "coupon_issue_list"

