from django.shortcuts import render
from userauths.models import UserProfile
# Create your views here.
def index_map(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/index-map.html",context)

def heat_map(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/heat-map.html",context)

def cluster_map(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/cluster-map.html",context)

def env_map(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/env-map.html",context)

def analyze(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/analyze.html",context)

