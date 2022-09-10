from django.db import models

from apps.users.models import User


class WantedData(models.Model):
    delivery_state = models.ForeignKey("orders.DeliveryState", on_delete=models.CASCADE)
    buyer          = models.ForeignKey(User, on_delete=models.CASCADE)
    pay_state      = models.CharField(max_length=50)
    quantity       = models.IntegerField()
    price          = models.DecimalField(max_digits = 8, decimal_places = 2)
    date           = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "wanted_data"


class DeliveryState(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "delivery_state"


class CountryCode(models.Model):
    country_code  = models.CharField(max_length=30)
    country_dcode = models.CharField(max_length=30)
    country_name  = models.CharField(max_length=50)

    class Meta:
        db_table = "country_code"


class DeliveryInfo(models.Model):
    countyr_code = models.ForeignKey("orders.CountryCode", on_delete=models.CASCADE)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    city_name    = models.CharField(max_length=50, null=True)
    zipx         = models.CharField(max_length=50)

    class Meta:
        db_table = "delivery_info"
