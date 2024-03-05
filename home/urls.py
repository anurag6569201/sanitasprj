from django.urls import path
from home import views
from plofile.context_process import send_message

app_name="home"

urlpatterns=[
    path('',views.index,name='index'),
    path('mark-all-as-read/', views.mark_all_as_read, name='mark_all_as_read'),
    path('send-message/', send_message, name='send_message'),
]
