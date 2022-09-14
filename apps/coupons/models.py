from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Coupon(models.Model):
    coupon_type = models.ForeignKey("coupons.CouponType", on_delete=models.CASCADE)
    coupon_num  = models.IntegerField(validators=[MinValueValidator(999999999),MaxValueValidator(5000000000)])


    class Meta:
        db_table = "coupons"


class CouponType(models.Model):
    type_name  = models.CharField(max_length=45)
    type_value = models.IntegerField(validators=[MinValueValidator(0)], null=True)

    class Meta:
        db_table = "coupon_types"


class CouponIssueList(models.Model):
    user   = models.ForeignKey("users.User", on_delete=models.CASCADE)
    coupon = models.ForeignKey("coupons.Coupon", on_delete=models.CASCADE)
    is_use = models.BooleanField(default=False)

    class Meta:
        db_table = "coupon_issue_list"

