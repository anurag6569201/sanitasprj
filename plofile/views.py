from django.shortcuts import render
from plofile.models import UserProfile

from userauths.models import UserProfile
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from plofile.forms import UserProfileForm

from creation.models import Post

# Create your views here.
def profile(request):
    userprofile=UserProfile.objects.get(user=request.user)
    userposts= Post.objects.filter(author=request.user)
    blogs=Post.objects.filter(author=request.user)
    context={
        "blogs":blogs,
        'userposts':userposts,
        'userprofile':userprofile,
        'user_profile':userprofile,
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
    return render(request,"plofile/sanitizer.html")

def tc(request):
    return render(request,"plofile/t&c.html")