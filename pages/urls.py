from django.urls import path
from .views import HomePageView, AboutPageView, homePageView, practice_view  #new
from .views import DashboardView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), #new
    path('', HomePageView.as_view(), name='home'),
    path('home2/', homePageView, name='home2'),
    path('practice/', practice_view, name='practice'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
