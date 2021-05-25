from django.test import SimpleTestCase
from django.urls import reverse, resolve
from eMenu_API import views


class TestUrls(SimpleTestCase):

    def test_menu_create_url(self):
        url = reverse('create-menu')
        self.assertEquals(resolve(url).func.view_class, views.CreateMenu)


    def test_menu_update_url(self):
        url = reverse('update-menu', args=[0])
        self.assertEquals(resolve(url).func.view_class, views.UpdateMenu)


    def test_menu_delete_url(self):
        url = reverse('delete-menu', args=[0])
        self.assertEquals(resolve(url).func.view_class, views.DeleteMenu)


    def test_dish_create_url(self):
        url = reverse('create-dish')
        self.assertEquals(resolve(url).func.view_class, views.CreateDish)


    def test_dish_update_url(self):
        url = reverse('update-dish', args=[0])
        self.assertEquals(resolve(url).func.view_class, views.UpdateDish)


    def test_dish_delete_url(self):
        url = reverse('delete-dish', args=[0])
        self.assertEquals(resolve(url).func.view_class, views.DeleteDish)


    def test_menu_list_url(self):
        url = reverse('list-menus')
        self.assertEquals(resolve(url).func.view_class, views.MenuList)