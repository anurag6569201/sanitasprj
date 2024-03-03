from django.urls import path
from home import views
from plofile.context_process import send_message

app_name="home"

urlpatterns=[
    path('',views.index,name='index'),
    path('send-message/', send_message, name='send_message'),
]
