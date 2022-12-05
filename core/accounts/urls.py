from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('myprofile/', views.myprofile, name="myprofile"),
    path('updateprofile/', views.updateprofile, name="updateprofile"),
    path('', views.home, name="home"),
    path('home1', views.home1, name="home1"),
]
