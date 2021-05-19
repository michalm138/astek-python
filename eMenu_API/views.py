from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models, serializers

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