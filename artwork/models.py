from django.db import models
from django.utils import timezone


# Create your models here.

class Oner(models.Model):
    oner_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.IntegerField()
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/')
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_img = models.ImageField(upload_to='media/')
    email = models.EmailField()
    contact = models.IntegerField()
    city = models.CharField(max_length=200)
    pin_code = models.IntegerField(max_length=200)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


class Product(models.Model):
    pro_id = models.AutoField(primary_key=True)
    panting_title = models.CharField(max_length=200)
    panting_img = models.ImageField(upload_to='media/')
    panting_by = models.CharField(max_length=200)
    panting_rate = models.IntegerField(default='free')

    def __str__(self):
        return self.panting_title

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    pro_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    STATUS = (("1", "active"), ("0","dactive"))
    order_status = models.CharField(max_length=20,choices=STATUS)
    order_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pro_id.panting_title
