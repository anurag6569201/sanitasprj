from django.contrib import admin
from .models import Sanitizer,TrendingData

# Register your models here.

class SanitizerAdmin(admin.ModelAdmin):
    list_display=['user','email','city']

admin.site.register(Sanitizer,SanitizerAdmin)

class TrendingDataAdmin(admin.ModelAdmin):
    list_display=['user','created_at']

admin.site.register(TrendingData,TrendingDataAdmin)