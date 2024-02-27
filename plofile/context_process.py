from plofile.models import Sanitizer

def sanitizer_glb(request):
    sanitizer_obj = None 
    
    if request.user.is_authenticated:
        sanitizer_obj, created = Sanitizer.objects.get_or_create(user=request.user)
    
    return {
        'sanitizer_obj': sanitizer_obj,
    }