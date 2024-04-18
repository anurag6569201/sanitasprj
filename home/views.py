from django.shortcuts import render
from home.models import recentUpdates

from django.contrib.auth.decorators import login_required
from home.models import Notification,spherepost
from django.shortcuts import redirect
from django.urls import reverse
from home.forms import sphereForm
from advertise.models import advertisement,sponsor,partnership
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View

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
    advertise=advertisement.objects.all()
    partner=partnership.objects.all()
    spnsr=sponsor.objects.all()

    liked_events = []
    liked_events = spherepost.objects.filter(likes=request.user)
    
    context = {
        'sphereform': sphere_form,
        'recentUpdate': recentUpdate,
        'topsphere': topsphere,
        'advertisement': advertise,
        'partner': partner,
        'sponsor': spnsr,
        'liked_events': liked_events,
    }
    return render(request, "home/index.html", context)

@login_required(login_url='userauths:sign-in')
def mark_all_as_read(request):
    notifications = Notification.objects.filter(recipient=request.user)
    for notification in notifications:
        notification.is_read = True
        notification.save()
    return redirect(reverse('home:index'))

class LikeEvent(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        event = get_object_or_404(spherepost, pk=self.kwargs['event_id'])
        event.like(request.user)
        return HttpResponseRedirect(reverse('home:sphere_comment', args=[str(event.id)]))
    

def sphere_comment(request, event_id):
    advertise=advertisement.objects.all()
    partner=partnership.objects.all()
    spnsr=sponsor.objects.all()
    context = {
        'advertisement': advertise,
        'partner': partner,
        'sponsor': spnsr,
    }
    return render(request, "home/comment.html",context)