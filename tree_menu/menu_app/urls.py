from django.urls import path

from .views import HomePageView


app_name = 'menu'

urlpatterns = [
    path('menu/', HomePageView.as_view(), name='home')
]