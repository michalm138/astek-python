from django.urls import path
from . import views
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="eMenu API",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact(email="michalmichalak138@gmail.com"),
   ),
   public=False,
   permission_classes=(permissions.IsAuthenticated,),
)


urlpatterns = [
    # Private API endpoints
    path('private/create/menu/', views.CreateMenu.as_view(), name='create-menu'),
    path('private/delete/menu/<int:pk>/', views.DeleteMenu.as_view(), name='delete-menu'),
    path('private/update/menu/<int:pk>/', views.UpdateMenu.as_view(), name='update-menu'),
    path('private/create/dish/', views.CreateDish.as_view(), name='create-dish'),
    path('private/delete/dish/<int:pk>/', views.DeleteDish.as_view(), name='delete-dish'),
    path('private/update/dish/<int:pk>/', views.UpdateDish.as_view(), name='update-dish'),
    # Public API endpoints
    path('public/list/menus/', views.MenuList.as_view(), name='list-menus'),
    # Other
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
