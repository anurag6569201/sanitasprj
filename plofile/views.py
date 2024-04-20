from django.shortcuts import render
from plofile.models import Sanitizer,TrendingData
from userauths.models import UserProfile

from userauths.models import UserProfile
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from plofile.forms import UserProfileForm,SanitizerForm,SanitizerForm1

from creation.models import Post
from django.contrib import messages
from django.shortcuts import redirect

from .forms import DiseaseFormSet
from django.contrib.auth.decorators import login_required

from home.models import spherepost

# Create your views here.
@login_required(login_url='userauths:sign-in')
def profile(request):
    userprofile=UserProfile.objects.get(user=request.user)
    userposts= Post.objects.filter(author=request.user)
    blogs=Post.objects.filter(author=request.user)
    topsphere = spherepost.objects.filter(author=request.user)
    
    liked_events = []
    liked_events = spherepost.objects.filter(likes=request.user)

    sanitizer_obj, created = Sanitizer.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        formset = DiseaseFormSet(request.POST)
        if formset.is_valid():
            trending_data = TrendingData.objects.create(user=request.user, city=sanitizer_obj.city, state=sanitizer_obj.state)
            for form in formset:
                if form.has_changed():
                    disease = form.save(commit=False)
                    disease.trending_data = trending_data  
                    disease.save()
                    messages.success(request, f"Data submitted successfully!!")
            return redirect('plofile:index-profile') 
    else:
        formset = DiseaseFormSet()

    context={
        "blogs":blogs,
        'userposts':userposts,
        'userprofile':userprofile,
        'user_profile':userprofile,
        'sanitizer_obj':sanitizer_obj,
        'formset': formset,
        'topsphere':topsphere,
        'liked_events': liked_events,
    }
    return render(request,"plofile/index-profile.html",context)

@login_required(login_url='userauths:sign-in')
def UserProfileUpdateView(request):
    template_name = 'plofile/edit_profile.html'
    success_url = reverse_lazy('plofile:index-profile')

    user_profile = UserProfile.objects.get(user=request.user)
    sanitizer_obj = Sanitizer.objects.get(user=request.user)
    form1=None
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        form1 = SanitizerForm(request.POST, request.FILES, instance=sanitizer_obj)
        if form.is_valid():
            form.save()
            return redirect(success_url)
        if sanitizer_obj.isSubmitted:
            if form1.is_valid():
                form1.save()
                return redirect(success_url)
    else:
        form = UserProfileForm(instance=user_profile)
        if sanitizer_obj.isSubmitted:
            form1 = SanitizerForm(instance=sanitizer_obj)

    context = {
        'form': form,
        'sanitizer_form': form1,
        'userprofile': user_profile,
        'user_profile': user_profile,
        'sanitizer_obj':sanitizer_obj,
    }

    return render(request, template_name, context)
    
@login_required(login_url='userauths:sign-in')
def sanitizer(request):
    sanitizer_obj, created = Sanitizer.objects.get_or_create(user=request.user)
    if not sanitizer_obj.isSubmitted:
        Sform = SanitizerForm1(request.POST, request.FILES,instance=sanitizer_obj)
        if request.method == "POST":
            form = SanitizerForm1(request.POST, request.FILES,instance=sanitizer_obj)
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

@login_required(login_url='userauths:sign-in')
def tc(request):
    return render(request,"plofile/t&c.html")

@login_required(login_url='userauths:sign-in')
def success(request):
    return render(request,"plofile/success.html")
