from django.urls import path
from . import views

urlpatterns = [
    path('public/hello_world/', views.hello_world, name='hello-world'),
]
