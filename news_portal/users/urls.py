from django.urls import path
from . import views

urlpatterns = [
    # Пока можно оставить пустым или добавить временные пути
    path('', views.home, name='users_home'),
]