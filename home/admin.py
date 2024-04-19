from django.contrib import admin
from .models import recentUpdates,Notification,spherepost,Question,Choice


admin.site.register(recentUpdates)
admin.site.register(Notification)
admin.site.register(spherepost)
admin.site.register(Question)
admin.site.register(Choice)