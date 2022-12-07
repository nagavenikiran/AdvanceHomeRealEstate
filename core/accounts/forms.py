from django import forms
from .models import UserProfile
from django.forms import ModelForm
import django_filters
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Property_images


class UserModify(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "address",
            "useremail",
            "mobile",
            "aboutme"

        ]
class Property_images(forms.ModelForm):
    class Meta:
        model = Property_images
        fields = ('prop_image_name', 'listing', 'image')