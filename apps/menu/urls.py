from django.urls import path
from apps.menu.views import menu

urlpatterns = [
    path('menu/', menu, name = 'menu'),
]
