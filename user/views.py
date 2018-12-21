from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

from social_django.models import UserSocialAuth

# Create your views here.

def home(request):
    if request.user.is_authenticated:

        return render(request,'user/home.html',{'message': 'Hi there!'})
    else:
        return render(request,'home.html',{'message': 'Hi there!'})