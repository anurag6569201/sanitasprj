from django.shortcuts import render

# Create your views here.
def index_map(request):
    return render(request,"map/index-map.html")