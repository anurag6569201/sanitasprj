import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from plofile.models import Sanitizer,Disease,TrendingData
from django.db.models import Sum
from django.utils import timezone
from home.models import Notification
from django.shortcuts import redirect
from django.shortcuts import render
from userauths.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

def sanitizer_glb(request):
    sanitizer_obj = None 
    userProf = None 
    Chatapi="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"
    
    if request.user.is_authenticated:
        sanitizer_obj, created = Sanitizer.objects.get_or_create(user=request.user)
        try:
            userProf = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            profile_image_url = "profile_images/default_profile_image.jpg"
            userProf = UserProfile.objects.create(user=request.user, profile_image=profile_image_url)
        except IntegrityError:
            userProf = UserProfile.objects.get(user=request.user)

    
    return {
        'sanitizer_obj': sanitizer_obj,
        'Chatapi':Chatapi,
        'user_profile':userProf,
    }

def dataCalculation(request):
    if 'city' in request.GET and 'state' in request.GET:
        city = request.GET.get('city')
        state = request.GET.get('state')
    else:
        city = "Bhubaneswar"
        state = "Odisha"

    last_24_hours = timezone.now() - timezone.timedelta(hours=24)
    last_7_days = timezone.now() - timezone.timedelta(days=7)
    sanit = Sanitizer.objects.all()
    
    unique_disease_24hr = Disease.objects.filter(trending_data__created_at__gte=last_24_hours, trending_data__city=city, trending_data__state=state).values('name').annotate(total_cases=Sum('cases'))
    unique_disease_24hr = {disease_case['name']: disease_case['total_cases'] for disease_case in unique_disease_24hr}

    unique_disease_7days = Disease.objects.filter(trending_data__created_at__gte=last_7_days).values('name').annotate(total_cases=Sum('cases'))
    unique_disease_7days = {disease_case['name']: disease_case['total_cases'] for disease_case in unique_disease_7days}

    total_cases_24hr = sum(unique_disease_24hr.values())

    top_diseases_24hr = sorted(unique_disease_24hr.items(), key=lambda x: x[1], reverse=True)[:7]
    All_diseases_24hr = sorted(unique_disease_24hr.items(), key=lambda x: x[1], reverse=True)
    top_diseases_7days = sorted(unique_disease_7days.items(), key=lambda x: x[1], reverse=True)[:7]

    response_data = {
        'top_diseases': top_diseases_24hr,
        'top_diseases_7days': top_diseases_7days,
        'sanit': sanit,
        'total_cases_24hr': total_cases_24hr,
        'All_diseases_24hr': All_diseases_24hr,
    }
    return response_data

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '')

        if message:
            try:
                api_key = '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'  # Replace this with your OpenAI API key
                response = requests.post('https://api.openai.com/v1/chat/completions',
                                         headers={'Authorization': f'Bearer {api_key}',
                                                  'Content-Type': 'application/json'},
                                         json={
                                             'model': 'gpt-3.5-turbo-0125',
                                             'messages': [
                                                 {'role': 'system', 'content': 'Doctor'},
                                                 {'role': 'user', 'content': message}
                                             ]
                                         })
                data = response.json()
                assistant_reply = data['choices'][0]['message']['content']
                return JsonResponse({'reply': assistant_reply})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'No message provided'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    

def notification(request):
    if request.user.is_authenticated:
        current_user = request.user
        last_24_hours = timezone.now() - timezone.timedelta(hours=24)
        notify_24hr = Notification.objects.filter(recipient=current_user, timestamp__gte=last_24_hours).order_by('-timestamp')
        has_unread_notifications = any(notif.is_read == False for notif in notify_24hr)
        return {
            'notify_24hr': notify_24hr,
            'has_unread_notifications': has_unread_notifications,
        }
    else:
        return {} 
    

from opencage.geocoder import OpenCageGeocode
from pprint import pprint
import requests

def get_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        if 'loc' in data:
            latitude, longitude = data['loc'].split(',')
            return float(latitude), float(longitude)
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

def location_context(request):
    key = '3313e90e58b54045a71c161530e9cb01'
    geocoder = OpenCageGeocode(key)

    location = get_location()

    city = ''
    state = ''
    if location:
        results = geocoder.reverse_geocode(location[0], location[1])
        if results and len(results):
            components = results[0]['components']
            city = components.get('city', '')
            state = components.get('state', '')

    return {
        'current_city': city,
        'current_state': state,
    }