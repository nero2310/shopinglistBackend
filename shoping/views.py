from rest_framework import viewsets, status
from rest_framework.generics import ListCreateAPIView,DestroyAPIView
from rest_framework.response import Response

from .models import Language, Shopping, Item, ShoppingItem
from .serializers import LanguageSerializer, ShoppingSerializer, ItemSerializer, ShoppingItemSerializer, \
    CreateShoppingItemSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ShoppingViewSet(ListCreateAPIView,DestroyAPIView):
    queryset = Shopping.objects.all()
    serializer_class = ShoppingSerializer


class ItemViewSet(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ShoppingItemViewSet(ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateShoppingItemSerializer
        return ShoppingItemSerializer

    def get_queryset(self):
        return ShoppingItem.objects.filter(shopping_id=self.kwargs.get('pk'))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        new_serializer = ShoppingItemSerializer(instance=ShoppingItem.objects.get(pk=serializer.data['pk']), many=False)
        print(new_serializer.data)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
