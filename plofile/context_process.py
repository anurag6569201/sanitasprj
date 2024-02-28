from plofile.models import Sanitizer,Disease
from django.db.models import Sum

def sanitizer_glb(request):
    sanitizer_obj = None 
    
    if request.user.is_authenticated:
        sanitizer_obj, created = Sanitizer.objects.get_or_create(user=request.user)
    
    return {
        'sanitizer_obj': sanitizer_obj,
    }

def dataCalculation(request):
    unique_disease_cases = Disease.objects.values('name').annotate(total_cases=Sum('cases'))
    unique_disease_dict = {disease_case['name']: disease_case['total_cases'] for disease_case in unique_disease_cases}

    top_diseases = sorted(unique_disease_dict.items(), key=lambda x: x[1], reverse=True)[:7]

    return {
        'unique_disease_dict': unique_disease_dict,
        'top_diseases': top_diseases
    }