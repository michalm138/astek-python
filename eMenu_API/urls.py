from django.urls import path
from . import views

urlpatterns = [
    # Private API endpoints
    path('private/create/menu/', views.CreateMenu.as_view(), name='create-menu'),
    path('private/delete/menu/<int:pk>/', views.DeleteMenu.as_view(), name='delete-menu'),
    path('private/update/menu/<int:pk>/', views.UpdateMenu.as_view(), name='update-menu'),
    path('private/create/dish/', views.CreateDish.as_view(), name='create-dish'),
    path('private/delete/dish/<int:pk>/', views.DeleteDish.as_view(), name='delete-dish'),
    path('private/update/dish/<int:pk>/', views.UpdateDish.as_view(), name='update-dish'),
    # Publuc API endpoints
]
