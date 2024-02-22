from django.urls import path
from material import views

app_name="material"

urlpatterns=[
    path('',views.material_index,name='index-material'),
]