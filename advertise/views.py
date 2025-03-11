from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def disease_data(request):
    # Dummy data for diseases
    diseases = [
        {"name": "Dengue", "cases": 150},
        {"name": "Malaria", "cases": 120},
        {"name": "Typhoid", "cases": 100},
        {"name": "COVID-19", "cases": 200},
        {"name": "Cholera", "cases": 80},
    ]

    total_cases = sum(disease["cases"] for disease in diseases)

    return JsonResponse({
        "top_diseases": diseases,
        "total_cases": total_cases
    })
