from django.urls import path
from plofile import views
from .views import UserProfileUpdateView
app_name="plofile"

urlpatterns=[
    path("",views.profile,name="index-profile"),
    path('profile/edit', UserProfileUpdateView.as_view(), name='verifier_edit'),
]