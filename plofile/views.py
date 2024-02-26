from django.shortcuts import render
from plofile.models import UserProfile,Sanitizer

from userauths.models import UserProfile
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from plofile.forms import UserProfileForm,SanitizerForm

from creation.models import Post
from django.contrib import messages
from django.shortcuts import redirect

from django.utils import timezone
from django.db.models import Count,Q
from .forms import TrendingDataForm
from .models import TrendingData
# Create your views here.
def profile(request):
    userprofile=UserProfile.objects.get(user=request.user)
    userposts= Post.objects.filter(author=request.user)
    blogs=Post.objects.filter(author=request.user)
    sanitizer_obj, created = Sanitizer.objects.get_or_create(user=request.user)
    context={
        "blogs":blogs,
        'userposts':userposts,
        'userprofile':userprofile,
        'user_profile':userprofile,
        'sanitizer_obj':sanitizer_obj,
    }
    return render(request,"plofile/index-profile.html",context)

class UserProfileUpdateView(FormView):
    template_name = 'plofile/edit_profile.html'

    form_class = UserProfileForm
    success_url = reverse_lazy('plofile:index-profile')

    def get_form_kwargs(self):
        kwargs = super(UserProfileUpdateView, self).get_form_kwargs()
        kwargs['instance'] = UserProfile.objects.get(user=self.request.user)
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UserProfileUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
        context['userprofile'] = UserProfile.objects.get(user=self.request.user)
        context['user_profile']=UserProfile.objects.get(user=self.request.user)
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user:
            self.template_name = 'plofile/edit_profile.html'
            self.success_url = reverse_lazy('plofile:index-profile')
        else:
            self.template_name = 'plofile/edit_profile.html'
            self.success_url = reverse_lazy('plofile:index-profile')

        return super(UserProfileUpdateView, self).dispatch(request, *args, **kwargs)
    
def sanitizer(request):
    sanitizer_obj, created = Sanitizer.objects.get_or_create(user=request.user)
    if not sanitizer_obj.isSubmitted:
        Sform = SanitizerForm(instance=sanitizer_obj)
        if request.method == "POST":
            form = SanitizerForm(request.POST, instance=sanitizer_obj)
            if form.is_valid():
                sanitizer_obj.isSubmitted=True
                form.save()
                messages.success(request, f"Hey, your request for becoming a sanitizer submitted successfully")
                if not sanitizer_obj.is_verified:
                    return redirect("plofile:success")
        context = {
            'sform': Sform,
        }
    else:
        return redirect("plofile:success")
    return render(request, "plofile/sanitizer.html", context)

def tc(request):
    return render(request,"plofile/t&c.html")

def success(request):
    return render(request,"plofile/success.html")

def post_trending_data(request):
    user = request.user
    last_post_time = TrendingData.objects.filter(user=user).aggregate(last_post_time=Count('created_at', filter=Q(created_at__gte=timezone.now() - timezone.timedelta(days=1))))
    
    if request.method == 'POST':
        form = TrendingDataForm(request.POST)
        if form.is_valid():
            trending_data = form.save(commit=False)
            trending_data.user = request.user
            trending_data.save()
            return redirect('plofile:index-profile')
    else:
        form = TrendingDataForm()
    return redirect('plofile:index-profile', {'form': form,'last_post_time':last_post_time['last_post_time']})
