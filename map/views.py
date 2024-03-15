from django.shortcuts import render
from userauths.models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='userauths:sign-in')
def index_map(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/index-map.html",context)

@login_required(login_url='userauths:sign-in')
def heat_map(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/heat-map.html",context)

@login_required(login_url='userauths:sign-in')
def cluster_map(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/cluster-map.html",context)

@login_required(login_url='userauths:sign-in')
def env_map(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/env-map.html",context)

@login_required(login_url='userauths:sign-in')
def analyze(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/analyze.html",context)

