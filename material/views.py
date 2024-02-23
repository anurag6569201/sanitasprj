from django.shortcuts import render
import requests
from django.utils.html import escape
from django.http import JsonResponse

# Create your views here.
def material_index(request):
    return render(request,"material/index-material.html")

import xml.etree.ElementTree as ET
import requests

def disease(request):
    input_disease = request.GET.get('q', 'diabetes')
    api_call_url = f"https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term={input_disease}&rettype=all"
    response = requests.get(api_call_url)
    xml_content = response.content.decode("utf-8")

    root = ET.fromstring(xml_content)

    data = {
        "title": root.find("./term").text,
        "description": [],
        "prevention": [],
    }

    for summary in root.findall(".//content[@name='FullSummary']"):
        data["description"].append(summary.text)

    for group in root.findall(".//content[@name='groupName']"):
        data["prevention"].append(group.text)

    data["description"] = " ".join(data["description"])

    context = {
        "data": data,
    }

    return render(request, "material/disease-search.html", context)
