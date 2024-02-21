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
    return render(request,"map/heat-map.html")

def cluster_map(request):
    return render(request,"map/cluster-map.html")

def env_map(request):
    return render(request,"map/env-map.html")

def analyze(request):
    return render(request,"map/analyze.html")

