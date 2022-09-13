from django.db import models


class Coupon(models.Model):
    coupon_type = models.ForeignKey("coupons.CouponType", on_delete=models.CASCADE)
    coupon_num  = models.IntegerField()

    class Meta:
        db_table = "coupons"


class CouponType(models.Model):
    type_name = models.CharField(max_length=45)

    class Meta:
        db_table = "coupon_types"


class CouponIssueList(models.Model):
    user   = models.ForeignKey("users.User", on_delete=models.CASCADE)
    coupon = models.ForeignKey("coupons.Coupon", on_delete=models.CASCADE)
    is_use = models.BooleanField(default=False)

    class Meta:
        db_table = "coupon_issue_list"

