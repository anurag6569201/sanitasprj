from django.shortcuts import render
from creation.models import Post
from userauths.models import UserProfile
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from home.models import recentUpdates

from django.contrib.auth.decorators import login_required
from home.models import Notification
from django.shortcuts import redirect
from django.urls import reverse

@login_required(login_url='userauths:sign-in')
def index(request):
    posts = Post.objects.all()
    user_profile = None
    if request.user.is_authenticated:
        blogs=Post.objects.all()
        recentUpdate=recentUpdates.objects.all()
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
        'recentUpdate':recentUpdate,
    }
    return render(request, "home/index.html", context)

def mark_all_as_read(request):
    notifications = Notification.objects.filter(recipient=request.user)
    for notification in notifications:
        notification.is_read = True
        notification.save()
    return redirect(reverse('home:index'))