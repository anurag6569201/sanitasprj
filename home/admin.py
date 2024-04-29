from django.contrib import admin
from .models import recentUpdates,Notification,spherepost,sphereComment


admin.site.register(recentUpdates)
admin.site.register(Notification)
admin.site.register(spherepost)
admin.site.register(sphereComment)