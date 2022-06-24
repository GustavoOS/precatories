from django.urls import path

from .views.signup import signup_view

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', signup_view, name='index'),
]
