from django.urls import path
from material import views

app_name="material"

urlpatterns=[
    path('',views.material_index,name='index-material'),
    path('disease',views.disease,name='disease'),
    path('calorie',views.calorie,name='calorie'),
    path('resource',views.resource,name='resource'),
    path('medic',views.medicine,name='medicine'),
]