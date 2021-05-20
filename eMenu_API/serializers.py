from rest_framework import serializers
from . import models

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Menu
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dish
        fields = '__all__'


class MenuListSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)

    class Meta:
        model = models.Menu
        fields = [
            'id',
            'name',
            'description',
            'creation_date',
            'update_date',
            'dishes_count',
            'dishes',
        ]
