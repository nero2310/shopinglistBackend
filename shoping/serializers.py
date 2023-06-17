from rest_framework import serializers
from .models import Language, Shopping, Item, ItemTranslations, ShoppingItem


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'short_code']


class ItemTranslationsSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = ItemTranslations
        fields = ['name', 'language']


class ItemSerializer(serializers.ModelSerializer):
    item_translations = ItemTranslationsSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'unit_price', 'item_translations']


class ShoppingSerializer(serializers.ModelSerializer):
    item_count = serializers.SerializerMethodField(read_only=True)
    total_item_price= serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Shopping
        fields = ['id', 'name', 'created_at', 'modified_at', 'item_count','total_item_price']

    def get_item_count(self, instance):
        return Item.objects.filter(shoppingitem__shopping=instance).count()

    def get_total_item_price(self, instance):
        total_price = 0
        for item in ShoppingItem.objects.filter(shopping=instance):
            total_price += item.quantity * item.item.unit_price
        return total_price


class ShoppingItemSerializer(serializers.ModelSerializer):
    shopping = ShoppingSerializer()
    item = ItemSerializer()

    class Meta:
        model = ShoppingItem
        fields = ['pk', 'shopping', 'item', 'quantity']


class CreateShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ['pk', 'shopping', 'item', 'quantity']
