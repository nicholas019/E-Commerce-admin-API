from rest_framework import serializers

from apps.orders.models import WantedData


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantedData
        fields = ("pk", "quantity",  )



        delivery_state = models.ForeignKey("orders.DeliveryState", on_delete=models.CASCADE)
    buyer          = models.ForeignKey(User, on_delete=models.CASCADE)
    country_code   = models.ForeignKey("orders.CountryCode", on_delete=models.CASCADE)
    quantity       = models.IntegerField()
    price          = models.DecimalField(max_digits = 8, decimal_places = 2)
    created_at  