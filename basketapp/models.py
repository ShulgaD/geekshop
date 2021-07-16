from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.utils.functional import cached_property

from mainapp.models import Product


# class BasketQuerySet(models.QuerySet):
#
#     def delete(self):
#         for item in self:
#             item.product.quantity += item.quantity
#             item.product.save()
#         super().delete()


class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="basket")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('количество', default=0)
    add_datetime = models.DateTimeField('время', auto_now_add=True)
    update_datetime = models.DateTimeField('время', auto_now=True)

    # @cached_property
    # def get_items_cached(self):
    #     return self.user.basket.select_related()


    @property
    def product_cost(self):
        # _items = self.get_items_cached
        return self.product.price * self.quantity
        # return sum(list(map(lambda x: x.quntity, _items)))

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk)
        # return pk.basket.select_related().order_by('product__category')


    # def delete(self, *args, **kwargs):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super.delete(*args, **kwargs)
    #
    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         self.product.quantity += self.quantity - self.__class__.objects.get(pk=self.pk).quantity
    #     else:
    #         self.product.quantity += self.quantity
    #     super.save(*args, **kwargs)
