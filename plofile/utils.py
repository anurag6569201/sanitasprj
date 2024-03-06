from django.http import JsonResponse

def fetch_data(request):
    if request.method == 'GET' and 'city' in request.GET and 'state' in request.GET:
        city = request.GET.get('city')
        state = request.GET.get('state')
        print(city)
        print(state)
        return city,state
    return None,None