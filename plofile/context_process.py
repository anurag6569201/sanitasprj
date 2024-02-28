from plofile.models import Sanitizer,Disease
from django.db.models import Sum
from django.utils import timezone

def sanitizer_glb(request):
    sanitizer_obj = None 
    
    if request.user.is_authenticated:
        sanitizer_obj, created = Sanitizer.objects.get_or_create(user=request.user)
    
    return {
        'sanitizer_obj': sanitizer_obj,
    }

def dataCalculation(request):
    last_24_hours = timezone.now() - timezone.timedelta(hours=24)
    last_7_days = timezone.now() - timezone.timedelta(hours=168)

    unique_disease_24hr = Disease.objects.filter(created_at__gte=last_24_hours).values('name').annotate(total_cases=Sum('cases'))
    unique_disease_24hr = {disease_case['name']: disease_case['total_cases'] for disease_case in unique_disease_24hr}

    unique_disease_7days = Disease.objects.filter(created_at__gte=last_7_days).values('name').annotate(total_cases=Sum('cases'))
    unique_disease_7days = {disease_case['name']: disease_case['total_cases'] for disease_case in unique_disease_7days}

    top_diseases_24hr = sorted(unique_disease_24hr.items(), key=lambda x: x[1], reverse=True)[:7]
    top_diseases_7days = sorted(unique_disease_7days.items(), key=lambda x: x[1], reverse=True)[:7]
    return {
        'top_diseases': top_diseases_24hr,
        'top_diseases_7days': top_diseases_7days,
    }