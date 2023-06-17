from django.urls import path
from .views import LanguageViewSet, ShoppingViewSet, ItemViewSet, ShoppingItemViewSet

urlpatterns = [
    path('languages/', LanguageViewSet.as_view({'get': 'list', 'post': 'create'}), name='language-list'),
    path('languages/<int:pk>/', LanguageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='language-detail'),

    path('shoppings/', ShoppingViewSet.as_view(), name='shopping-list'),
    path('shoppings/<int:pk>', ShoppingViewSet.as_view(), name='shopping-list'),

    path('items/', ItemViewSet.as_view(), name='item-list'),

    path('shopping-items/', ShoppingItemViewSet.as_view(), name='shopping-item-list'),
    path('shopping-items/<int:pk>/', ShoppingItemViewSet.as_view(), name='shopping-item-detail'),
]
