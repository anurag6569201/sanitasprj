from django.shortcuts import render
from creation.models import Post
from userauths.models import UserProfile
# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url='userauths:sign-in')
def index(request):
    posts = Post.objects.all()
    user_profile = None
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'posts': posts,
        'user_profile': user_profile,
    }
    return render(request, "home/index.html", context)
