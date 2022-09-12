from django.db import models


class WantedData(models.Model):
    delivery_state = models.ForeignKey("orders.DeliveryState", on_delete=models.CASCADE)
    buyer          = models.ForeignKey("users.User", related_name="users", on_delete=models.CASCADE)
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
    
    def __str__(self):
        return f"{self.name}"


class CountryCode(models.Model):
    code  = models.CharField(max_length=30)
    dcode = models.CharField(max_length=30)
    name  = models.CharField(max_length=50)

    class Meta:
        db_table = "country_code"


class DeliveryInfo(models.Model):
    country_code = models.ForeignKey("orders.CountryCode", related_name="country_codes", on_delete=models.CASCADE)
    user         = models.ForeignKey("users.User", related_name="delivery_info", on_delete=models.CASCADE)
    city         = models.CharField(max_length=50, null=True)
    zipx         = models.CharField(max_length=50)

    class Meta:
        db_table = "delivery_info"
