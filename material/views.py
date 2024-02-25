from django.shortcuts import render
import requests
from django.utils.html import escape
from userauths.models import UserProfile
from django.http import JsonResponse

import xml.etree.ElementTree as ET
import requests

# Create your views here.
def material_index(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"material/index-material.html",context)

def disease(request):
    user_profile = UserProfile.objects.get(user=request.user)
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
        'user_profile': user_profile,
    }

    return render(request, "material/disease-search.html", context)


import requests
from django.shortcuts import render

def calorie(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'GET':
        input_dish = request.GET.get('dishes','egg')

    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    headers = {
        'Content-Type': 'application/json',
        'x-app-id': '86805170',
        'x-app-key': '4dea52376db1086b8ab3b5d0cdcc53c5',
    }
    data = {
        'query': input_dish,
    }

    response = requests.post(url, headers=headers, json=data)
    calorie_data = response.json()
    print(calorie_data)

    if 'foods' in calorie_data:
        foods = calorie_data['foods']
        tags = calorie_data['foods'][0]['tags']

        if len(foods) > 0:
            calories = foods[0]
            context = {
                'tags':tags,
                'calorie_data': calorie_data,
                'calories': calories,
                'user_profile': user_profile,
            }
            return render(request, "material/calorie.html", context)
        else:
            context = {
                'calorie_data': calorie_data,
                'error_message': 'No food found for the given query.',
            }
            return render(request, "material/calorie.html", context)
    else:
        context = {
            'calorie_data': calorie_data,
            'error_message': 'Error fetching data from Nutritionix API.',
        }
        return render(request, "material/calorie.html", context)

def resource(request):     
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }   
    return render(request,"material/resource.html",context)