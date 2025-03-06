from django.contrib import admin
from .models import Sanitizer,Disease,TrendingData
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class SanitizerAdmin(admin.ModelAdmin):
    list_display=['user','email','city']

admin.site.register(Sanitizer,SanitizerAdmin)


@admin.register(TrendingData)
class TrendingDataAdmin(ImportExportModelAdmin):
    list_display = ("user", 'id',"state", "city", "created_at")  # Display these fields in the admin panel
    list_filter = ("state", "city", "created_at")  # Add filters for better search
    search_fields = ("user__username", "state", "city")  # Enable searching by username, state, and city
    ordering = ("-created_at",)  # Order by most recent entries

@admin.register(Disease)
class DiseaseAdmin(ImportExportModelAdmin):
    list_display = ("name", "cases", "trending_data")  # Show relevant fields
    list_filter = ("name",)  # Filter by disease name
    search_fields = ("name",)  # Search by disease name
    ordering = ("-cases",)  # Order by highest cases first