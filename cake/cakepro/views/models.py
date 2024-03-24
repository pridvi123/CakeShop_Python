from django.db import models
 

class Cakes(models.Model):
    name=models.CharField(max_length=20)
    weight=models.CharField(max_length=20,default='1')
    cost=models.CharField(max_length=20)
    status=models.BooleanField(max_length=20,default=True,null=True)

class Customer(models.Model):
    name=models.CharField(max_length=20)
    mob=models.CharField(max_length=20)
    address=models.CharField(max_length=50)

class Order(models.Model):
    Cakes=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    Amount=models.IntegerField()
    TotalAmount = models.IntegerField(null=True, blank=True)

class UserCredentials(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)     