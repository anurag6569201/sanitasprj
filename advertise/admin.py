from django.contrib import admin

# Register your models here.
from advertise.models import advertisement,sponsor,partnership

admin.site.register(advertisement)
admin.site.register(sponsor)
admin.site.register(partnership)