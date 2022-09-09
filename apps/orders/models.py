from django.db import models

from apps.users.models import User


class WantedData(models.Model):
    pay_state  = models.ForeignKey("orders.PayState", on_delete=models.CASCADE)
    buyer      = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity   = models.IntegerField()
    price      = models.DecimalField(max_digits = 8, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "wanted_data"

class PayState(models.Model):
    status_name = models.CharField(max_length=30)

    class Meta:
        db_table = "pay_state"