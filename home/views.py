from django.shortcuts import render
from home.models import recentUpdates

from django.contrib.auth.decorators import login_required
from home.models import Notification,spherepost,sphereComment
from django.shortcuts import redirect
from django.urls import reverse
from home.forms import sphereForm,CommentForm
from advertise.models import advertisement,sponsor,partnership
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.views import View

from django.db.models import Sum
from django.db.models import Subquery, OuterRef

def main(request):
    return redirect(reverse('home:index'))

@login_required(login_url='userauths:sign-in')
def index(request):
    post=None
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

    comments = sphereComment.objects.order_by('-created_at').all()
    

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
        'comments': comments, 
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
    topsphere = spherepost.objects.filter(pk=event_id)

    post = get_object_or_404(spherepost, pk=event_id)
    comments = sphereComment.objects.filter(post=post)
    comment_form = CommentForm()
    
    liked_events = []
    liked_events = spherepost.objects.filter(likes=request.user)

    context = {
        'advertisement': advertise,
        'partner': partner,
        'sponsor': spnsr,
        'topsphere':topsphere,
        'comments': comments, 
        'comment_form': comment_form,
        'post_id':event_id,
        'liked_events': liked_events,
    }
    return render(request, "home/comment.html",context)


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(spherepost, pk=self.kwargs['event_id'])
        form = CommentForm(request.POST)

        if form.is_valid(): 
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
        
        return redirect('home:sphere_comment', event_id=post.id)

from django.shortcuts import get_object_or_404, redirect, HttpResponse
from django.contrib import messages

def spherepost_delete_view(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(spherepost, pk=pk)
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('plofile:index-profile')
    else:
        return HttpResponseNotAllowed(['POST'])