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
    photo = models.ImageField(upload_to='avatars/%Y/%m/%d/', default = "")
    phone = models.CharField(max_length = 20, default = "")
    rating = models.IntegerField(default = 0)
    areas = models.ManyToManyField(Area)
    def __str__(self):
        return self.user.username


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default = 0)
    price = models.FloatField()
    begin_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(blank=True, null=True)
    expected_date = models.DateTimeField(blank=True, null=True)
    rating = models.IntegerField(default = 0, blank=True,null=True)
    feedback = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.client.username

    def get_absolute_url(self):
        return reverse('master_orders-detail', args=[str(self.id)])


class OrderLine(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    master = models.ForeignKey('Master', on_delete=models.CASCADE, blank=True, null = True)
    brand_name = models.CharField(max_length = 20)
    device_name = models.CharField(max_length = 20)
    serial_id = models.CharField(max_length = 20)
    feedback = models.TextField(blank=True, null = True)
    trouble_description = models.TextField()
    status = models.IntegerField(default = 0)

    def __str__(self):
        return self.feedback

    def get_absolute_url(self):
        return reverse('orders')

class Comment(models.Model):
    content = models.TextField(verbose_name="Текст комментария")
    author = models.ForeignKey(User, null = True)
    order = models.ForeignKey(Order)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content


