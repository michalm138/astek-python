from django.test import TestCase, Client
from django.urls import reverse
from eMenu_API import models
from django.contrib.auth import get_user_model
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        User = get_user_model()
        user = User.objects.create_user(
            username='temp',
            password='temp'
        )

        self.menu = models.Menu.objects.create(
            id = 0,
            name = 'string',
            description = 'string'
        )

        self.dish = models.Dish.objects.create(
            id = 0,
            menu = self.menu,
            name = 'string',
            description = 'string',
            price = 10.00,
            preparation_time = 60,
            vegetarian = False
        )


    def test_menu_list(self):
        response = self.client.get(reverse('list-menus'))
        self.assertEquals(response.status_code, 200)

    
    # Tests for menus
    def test_menu_create_authenticated(self):
        self.client.login(username='temp', password='temp')
        response = self.client.post(reverse('create-menu'), {
            'name': 'unique string',
            'description': 'string',
        })

        self.assertEquals(response.status_code, 201)

    
    def test_menu_create_unauthenticated(self):
        response = self.client.post(reverse('create-menu'))
        self.assertEquals(response.status_code, 403)


    def test_menu_update_authenticated(self):
        self.client.login(username='temp', password='temp')
        response = self.client.patch(reverse('update-menu', args=[0]), {
            "id": 2,
            "name": "string",
            "description": "string",
        }, content_type='application/json')
        self.assertEquals(response.status_code, 200)

        response = self.client.put(reverse('update-menu', args=[0]), {
            "id": 2,
            "name": "string",
            "description": "string",
        }, content_type='application/json')
        self.assertEquals(response.status_code, 200)

    
    def test_menu_update_unauthenticated(self):
        response = self.client.patch(reverse('update-menu', args=[0]))
        self.assertEquals(response.status_code, 403)

        response = self.client.put(reverse('update-menu', args=[0]))
        self.assertEquals(response.status_code, 403)


    def test_menu_delete_authenticated(self):
        self.client.login(username='temp', password='temp')
        response = self.client.delete(reverse('delete-menu', args=[0]), content_type='application/json')
        self.assertEquals(response.status_code, 204)

    
    def test_menu_delete_unauthenticated(self):
        response = self.client.delete(reverse('delete-menu', args=[0]))
        self.assertEquals(response.status_code, 403)


    # Tests for dishes
    def test_dish_create_authenticated(self):
        self.client.login(username='temp', password='temp')
        response = self.client.post(reverse('create-dish'), {
            'menu': 0,
            'name': 'string',
            'description': 'string',
            'price': 10.00,
            'preparation_time': 60,
            'vegetarian': False
        })
        self.assertEquals(response.status_code, 201)


    def test_dish_create_unauthenticated(self):
        response = self.client.post(reverse('create-dish'))
        self.assertEquals(response.status_code, 403)


    def test_dish_update_authenticated(self):
        self.client.login(username='temp', password='temp')
        response = self.client.patch(reverse('update-dish', args=[0]), {
            'id': 0,
            'menu': 0,
            'name': 'string',
            'description': 'string',
            'price': 10.00,
            'preparation_time': 60,
            'vegetarian': False
        }, content_type='application/json')
        self.assertEquals(response.status_code, 200)

        response = self.client.put(reverse('update-dish', args=[0]), {
            'id': 0,
            'menu': 0,
            'name': 'string',
            'description': 'string',
            'price': 10.00,
            'preparation_time': 60,
            'vegetarian': False
        }, content_type='application/json')
        self.assertEquals(response.status_code, 200)


    def test_dish_update_unauthenticated(self):
        response = self.client.patch(reverse('update-dish', args=['0']))
        self.assertEquals(response.status_code, 403)

        response = self.client.put(reverse('update-dish', args=['0']))
        self.assertEquals(response.status_code, 403)


    def test_dish_delete_authenticated(self):
        self.client.login(username='temp', password='temp')
        response = self.client.delete(reverse('delete-dish', args=[0]), content_type='application/json')
        self.assertEquals(response.status_code, 204)


    def test_dish_delete_unauthenticated(self):
        response = self.client.delete(reverse('delete-dish', args=['0']))
        self.assertEquals(response.status_code, 403)
