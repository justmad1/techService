from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from mainApp.models import Area, Service


class Master(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone = models.CharField(max_length = 20, default = "")
    rating = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.username


class OrderList(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default = 0)
    price = models.FloatField()
    begin_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField()
    expected_date = models.DateTimeField()
    rating = models.IntegerField(default = 0)
    comment = models.TextField()

    def __str__(self):
        return self.comment


class OrderLine(models.Model):
    orderList = models.ForeignKey(OrderList, on_delete=models.CASCADE)
    service = models.OneToOneField(Service, on_delete=models.CASCADE)
    master = models.OneToOneField(Master, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length = 20)
    device_name = models.CharField(max_length = 20)
    serial_id = models.CharField(max_length = 20)
    comment = models.TextField()
    trouble_description = models.TextField()
    status = models.IntegerField(default = 0)

    def __str__(self):
        return self.service.name
