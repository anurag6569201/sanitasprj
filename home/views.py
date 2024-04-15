from django.shortcuts import render
from home.models import recentUpdates

from django.contrib.auth.decorators import login_required
from home.models import Notification
from django.shortcuts import redirect
from django.urls import reverse

@login_required(login_url='userauths:sign-in')
def index(request):
    recentUpdate=recentUpdates.objects.all()
    context = {
        'recentUpdate':recentUpdate,
    }
    return render(request, "home/index.html", context)

@login_required(login_url='userauths:sign-in')
def mark_all_as_read(request):
    notifications = Notification.objects.filter(recipient=request.user)
    for notification in notifications:
        notification.is_read = True
        notification.save()
    return redirect(reverse('home:index'))