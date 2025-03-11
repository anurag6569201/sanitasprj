from django.urls import path
from home import views
from plofile.context_process import send_message
from .views import LikeEvent,CommentCreateView

from home.api_views import SphereAPIView,SphereCommentsAPIView,RecentUpdateAPIView

app_name="home"

urlpatterns=[
    path('',views.main,name='main'),
    path('home/',views.index,name='index'),
    path('home/sphere/<int:event_id>/',views.sphere_comment,name='sphere_comment'),
    path('mark-all-as-read/', views.mark_all_as_read, name='mark_all_as_read'),
    path('send-message/', send_message, name='send_message'),

    # like dislike
    path('like/<int:event_id>/', LikeEvent.as_view(), name='like_event'),
    path('post/<int:event_id>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('spherepost/<int:pk>/delete/', views.spherepost_delete_view, name='spherepost_delete'),

    path('api/sphere/view/', SphereAPIView.as_view(), name='sphere-list'),
    path('api/sphere/comments/<int:sphere_id>/', SphereCommentsAPIView.as_view(), name='sphere-comments-list'),
    path('api/recent/updates/', RecentUpdateAPIView.as_view(), name='recent-updates'),
]
