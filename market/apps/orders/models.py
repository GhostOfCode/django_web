from django.db import models
from django.db.models.signals import post_save
from ..products.models import Product


class OrderStatus(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статус заказа'


class Order(models.Model):
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=32, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)  # total price for order
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(OrderStatus, blank=True, null=True, default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ {0} - {1}".format(self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Order, self).save()


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=9, decimal_places=2, default=0)  # price of one item
    total_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)  # price_per_item * nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.nmb * price_per_item

        super(ProductInOrder, self).save()


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    order_total_price = sum(item.total_price for item in all_products_in_order)
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, ProductInOrder)
