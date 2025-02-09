from django.conf import settings
from django.db import models
from django.utils import timezone
class UserCar(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, 
        blank=True,
    )
    car_nickname = models.CharField(max_length=100) 
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    prod_year = models.DateField()
    purchase_date = models.DateField()
    initial_milleage = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.car_nickname
    
class Refuel(models.Model):
    date = models.DateField(default=timezone.now())
    current_mileage = models.IntegerField()
    amount = models.FloatField()
    price = models.FloatField()
    car = models.ForeignKey(UserCar, on_delete=models.CASCADE)

    @property
    def total_cost(self):
        return self.price*self.amount
    

    
    
