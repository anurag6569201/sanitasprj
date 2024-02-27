from django.urls import path
from plofile import views
from .views import UserProfileUpdateView
app_name="plofile"

urlpatterns=[
    path("",views.profile,name="index-profile"),
    path("t&c",views.tc,name="t&c"),
    path("success",views.success,name="success"),
    path("sanitizer/",views.sanitizer,name="sanitizer"),
    path('profile/edit', views.UserProfileUpdateView, name='verifier_edit'),
]
