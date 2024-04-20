from django.urls import path
from home import views
from plofile.context_process import send_message
from .views import LikeEvent,CommentCreateView

app_name="home"

urlpatterns=[
    path('',views.index,name='index'),
    path('sphere/<int:event_id>/',views.sphere_comment,name='sphere_comment'),
    path('mark-all-as-read/', views.mark_all_as_read, name='mark_all_as_read'),
    path('send-message/', send_message, name='send_message'),

    # like dislike
    path('like/<int:event_id>/', LikeEvent.as_view(), name='like_event'),
    path('post/<int:event_id>/comment/', CommentCreateView.as_view(), name='comment-create')
]
