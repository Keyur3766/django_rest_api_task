
from django.urls import include, path
from rest_framework import routers
from .views import taskAPIView, taskPostView






urlpatterns = [
    #path('', include(router.urls)),
    
    path('task/all',taskAPIView.as_view()),
    path('task/new',taskPostView.as_view())
    
]