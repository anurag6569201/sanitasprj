from django.shortcuts import render
import requests
from django.utils.html import escape
from django.http import JsonResponse

# Create your views here.
def material_index(request):
    return render(request,"material/index-material.html")

def disease(request):
    inputDisease = "dengue"
    api_call_url = f"https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term=title:{inputDisease}"
    response = requests.get(api_call_url)
    xml_content = response.content.decode("utf-8")
    context = {
        "data": xml_content,
    }
    return render(request, "material/disease-search.html", context)
