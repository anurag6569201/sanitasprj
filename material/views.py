from django.shortcuts import render

# Create your views here.
def material_index(request):
    return render(request,"material/index-material.html")