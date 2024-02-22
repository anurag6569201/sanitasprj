from django.shortcuts import render
from creation.models import Post
from userauths.models import UserProfile
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url='userauths:sign-in')
def index(request):
    posts = Post.objects.all()
    user_profile = None
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        blogs=Post.objects.all()
        page=request.GET.get('page')
        num_of_items=2
        paginator=Paginator(blogs,num_of_items)

        try:
            blogs=paginator.page(page)
        except PageNotAnInteger:
            page=1
            blogs=paginator.page(page)
        except EmptyPage:
            page=paginator.num_pages
            blogs=paginator.page(page)

    context = {
        "blogs":blogs,
        "paginator":paginator,
        'posts': posts,
        'user_profile': user_profile,
    }
    return render(request, "home/index.html", context)
