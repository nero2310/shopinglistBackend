from django.db import models


# Create your models here.

class Language(models.Model):
    name = models.TextField()
    short_code = models.CharField(max_length=8)


class Shopping(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Item(models.Model):
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)
    name = models.TextField(blank=False,null=False)


class ItemTranslations(models.Model):
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE,)
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE,related_name='item_translations')
    name = models.TextField()


class ShoppingItem(models.Model):
    shopping = models.ForeignKey(to=Shopping, on_delete=models.CASCADE)
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=2, max_digits=10)
