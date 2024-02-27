from django.contrib import admin
from .models import Sanitizer,Disease,TrendingData

# Register your models here.

class SanitizerAdmin(admin.ModelAdmin):
    list_display=['user','email','city']

admin.site.register(Sanitizer,SanitizerAdmin)


admin.site.register(Disease)
admin.site.register(TrendingData)