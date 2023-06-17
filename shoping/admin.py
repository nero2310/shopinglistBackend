from django.contrib import admin
from .models import Language, Shopping, Item, ItemTranslations, ShoppingItem


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_code']
    search_fields = ['id', 'name', 'short_code']


@admin.register(Shopping)
class ShoppingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'modified_at']
    search_fields = ['id', 'name']


@admin.register(ItemTranslations)
class ItemTranslationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'language', 'item']
    search_fields = ['id', 'language__name', 'item__unit_price']


@admin.register(ShoppingItem)
class ShoppingItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'shopping', 'item', 'quantity']
    search_fields = ['id', 'shopping__name', 'item__unit_price']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'unit_price']  # Wyświetlane pola w liście obiektów
    list_editable = ['unit_price']  # Pola, które można edytować bezpośrednio z listy
    search_fields = ['id', 'unit_price']  # Pola, po których można wyszukiwać
    list_filter = ['unit_price']  # Filtry boczne w panelu administratora
    # Inne dostosowania, takie jak fieldsets, inlines, itp.
