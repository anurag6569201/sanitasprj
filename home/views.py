from django.shortcuts import render
from home.models import recentUpdates

from django.contrib.auth.decorators import login_required
from home.models import Notification,spherepost
from django.shortcuts import redirect
from django.urls import reverse
from home.forms import sphereForm

@login_required(login_url='userauths:sign-in')
def index(request):
    if request.method == 'POST':
        sphere_form = sphereForm(request.POST, request.FILES)
        if sphere_form.is_valid():
            post = sphere_form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        sphere_form = sphereForm()
    recentUpdate = recentUpdates.objects.all()
    topsphere = spherepost.objects.all()
    context = {
        'sphereform': sphere_form,
        'recentUpdate': recentUpdate,
        'topsphere': topsphere,
    }
    return render(request, "home/index.html", context)

@login_required(login_url='userauths:sign-in')
def mark_all_as_read(request):
    notifications = Notification.objects.filter(recipient=request.user)
    for notification in notifications:
        notification.is_read = True
        notification.save()
    return redirect(reverse('home:index'))