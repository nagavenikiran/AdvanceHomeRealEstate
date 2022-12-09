from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .forms import UserModify



def landingPage(request):
    #Update this with HTML page from Saikiran and Niha
    return render(request, 'accounts/homepage.html')

def aboutUs(request):
    return render(request,'accounts/AboutUs.html')

def searchListings(request):
    return render(request,'accounts/searchlistings.html')

def omahaEvents(request):
    return render(request,'accounts/omahaevents.html')

def visitorDetails(request):
    return render(request,'accounts/visitordetails.html')

def confirmationMessage(request):
    return render(request, 'accounts/confirmationmessage.html')

def filteredlistings(request):
    return render(request, 'accounts/filteredlistings.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def listing_list(request):
    listings = Listing.isVisible.all()
    return render(request,
                  'accounts/listing/list.html',
                  {'listings': listings})

# Might need to change second input variable from 'id' to 'address' if doesn't work
def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request,
                  'accounts/listing/detail.html',
                  {'listing': listing})


##Nagaveni Code

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)


def home1(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def myprofile(request):
    context = {}
    context["dataset"] = UserProfile.objects.all()
    return render(request, 'accounts/myprofile.html', context)

@login_required(login_url='login')
def updateprofile(request):
    context = {}
    id = 1
    obj = get_object_or_404(UserProfile, id=id)
    form = UserModify(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return render(request, 'accounts/myprofile.html', context)
    context["form"] = form
    return render(request, 'accounts/updateprofile.html', context)

def omahaevents_agent(request):
    return render(request,'accounts/omahaevents_agent.html')


