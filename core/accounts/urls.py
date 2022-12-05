from django.urls import path
from . import views
from django.views.generic import RedirectView

<<<<<<< HEAD
urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('myprofile/', views.myprofile, name="myprofile"),
    path('updateprofile/', views.updateprofile, name="updateprofile"),
    path('', views.home, name="home"),
    path('home1', views.home1, name="home1"),
=======
app_name = 'accounts'

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name="home"),
	path('', views.landingPage, name="landing"),
	path('landing', views.landingPage, name="landing"),
	path('AboutUs', views.aboutUs, name="AboutUs"),
	path('searchlistings', views.searchListings, name="searchListings"),
	path('omahaevents', views.omahaEvents, name="omahaevents"),
	path('visitordetails', views.visitorDetails, name="visitordetails"),
	path('confirmationmessage', views.confirmationMessage, name="confirmationmessage"),
	path('filteredlistings', views.filteredlistings, name="filteredlistings"),
	#listing views
	path('listings', views.listing_list, name='listing_list'),
	path('<int:id>', views.listing_detail, name='listing_detail'),


>>>>>>> main
]
