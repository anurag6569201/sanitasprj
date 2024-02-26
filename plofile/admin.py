from django.contrib import admin
from .models import UserProfile,Sanitizer

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['name','email','mobile_number']

admin.site.register(UserProfile,UserProfileAdmin)

class SanitizerAdmin(admin.ModelAdmin):
    list_display=['user','email','city']

admin.site.register(Sanitizer,SanitizerAdmin)