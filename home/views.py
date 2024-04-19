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

from django.db.models import Sum

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
    
    question = Question.objects.all()

    liked_events = []
    liked_events = spherepost.objects.filter(likes=request.user)
    
    context = {
        'sphereform': sphere_form,
        'recentUpdate': recentUpdate,
        'topsphere': topsphere,
        'liked_events': liked_events,
        'questions':question,
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

from .models import Question, Choice
from django.http import JsonResponse

def poll_vote(request):
    if request.method == 'POST' and request.is_ajax():
        choice_id = request.POST.get('choice')
        choice = Choice.objects.get(id=choice_id)
        choice.votes += 1
        choice.save()
        return JsonResponse({'message': 'Thank you for your vote!'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)