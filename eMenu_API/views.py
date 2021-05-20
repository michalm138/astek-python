from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models, serializers
from rest_framework import filters
from django_filters import rest_framework as drf_filters
import django_filters

# Managment views for menu
class CreateMenu(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class DeleteMenu(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Menu.objects.all()


class UpdateMenu(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


# Managment views for dish
class CreateDish(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Dish.objects.all()
    serializer_class = serializers.DishSerializer


class DeleteDish(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Dish.objects.all()


class UpdateDish(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Dish.objects.all()
    serializer_class = serializers.DishSerializer


# Public API view
class MenuOrdering(filters.OrderingFilter):

    def filter_queryset(self, request, queryset, view):

        ordering = self.get_ordering(request, queryset, view)
        if ordering:
            if 'dishes_count' in ordering or '-dishes_count' in ordering:
                objects = {menu:models.Dish.objects.filter(menu=menu).count() for menu in queryset}
                dishes_count = [count for obj, count in objects.items()]
                if ordering[0][0] == '-':
                    dishes_count.sort(reverse=True)
                else:
                    dishes_count.sort()

                queryset = []
                for item in dishes_count:
                    for obj, count in objects.items():
                        if item == count:
                            queryset.append(obj)
                            break
                    objects.pop(queryset[len(queryset)-1])
                return queryset
            else:
                return queryset.order_by(*ordering)

        return queryset


class MenuFilter(drf_filters.FilterSet):
    creation_date = django_filters.DateTimeFilter(field_name="creation_date", lookup_expr="gte")
    update_date = django_filters.DateTimeFilter(field_name="update_date", lookup_expr="gte")

    class Meta:
        model = models.Menu
        fields = ['name', 'creation_date', 'update_date']


class MenuList(ListAPIView):
    permission_classes = ()
    queryset = models.Menu.objects.filter(dishes__isnull=False).distinct()
    serializer_class = serializers.MenuListSerializer
    filter_backends = [drf_filters.DjangoFilterBackend, MenuOrdering]
    filterset_class = MenuFilter
    ordering_fields = ['name', 'dishes_count']
    ordering = ['id']
