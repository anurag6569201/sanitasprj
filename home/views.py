from django.shortcuts import render
from creation.models import Post
from userauths.models import UserProfile
# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url='userauths:sign-in')
def index(request):
    return render(request,"home/index.html")