from rest_framework import serializers
from . import models

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Menu
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dish
        fields = [
            'menu',
            'name',
            'description',
            'price',
            'preparation_time',
            'vegetarian',
        ]