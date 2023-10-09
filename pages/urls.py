from django.urls import path
from .views import HomePageView, AboutPageView, homePageView  #new

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), #new
    path('', HomePageView.as_view(), name='home'),
    path('home2', homePageView, name='home2'),
]
