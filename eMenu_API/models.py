from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    preparation_time = models.PositiveIntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    vegetarian = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name

