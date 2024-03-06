from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import logout
from home.models import Notification
# from userauths.models import User

User=settings.AUTH_USER_MODEL

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was created successfully")

            notification_message = f"Hey {username}, your account was created successfully"
            Notification.objects.create(recipient=new_user, message=notification_message)

            new_user = authenticate(username=form.cleaned_data['email'], 
                                    password=form.cleaned_data['password1'])
            
            login(request, new_user)
            return redirect("home:index")
    else:
        form=UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'userauths/sign-up.html', context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request,f"Hey, You are already Logged in")
        return redirect('home:index')
    else:
        if request.method=="POST":
            email=request.POST.get("email")
            password=request.POST.get("password")

            try:
                user=User.object.get(email=email)
            except:
                messages.warning(request,f"User with {email} does not exist")

            user=authenticate(request,email=email,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,"Your are logged in.")
                notification_message = f"Your are logged in."
                Notification.objects.create(recipient=request.user, message=notification_message)
                return redirect("home:index")
            
            else:
                messages.warning(request,"User Does not exist, create an accounnt")

    context={

    }
    return render(request,"userauths/sign-in.html",context)

def logout_view(request):
    notification_message = "You Logged-Out, successfully"
    Notification.objects.create(recipient=request.user, message=notification_message)
    logout(request)
    messages.success(request, "You Logged-Out, successfully")
    return redirect("userauths:sign-in")