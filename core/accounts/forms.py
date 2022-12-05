from django import forms
from .models import UserProfile


class UserModify(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "address",
            "useremail",
            "mobile",
            "aboutme"

        ]
