from datetime import timedelta

from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.
from django.utils.timezone import now


class ShopUser(AbstractUser):
    age = models.PositiveSmallIntegerField('возраст', null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    description = models.TextField('описание', blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def basket_price(self):
        return sum(el.product_cost for el in self.basket_set.all())

    def basket_quantity(self):
        return sum(el.quantity for el in self.basket_set.all())

    def is_activation_key_expired(self):
        if now() < self.activation_key_created + timedelta(hours=48):
            return False
        return True

