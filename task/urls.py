
from django.urls import include, path
from rest_framework import routers
from .views import taskAPIView, taskPostView



#router = routers.DefaultRouter()
#router.register(r'task/all', taskViewSet)


urlpatterns = [
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('task/all',taskAPIView.as_view()),
    path('task/new',taskPostView.as_view())
    #path('task/all',taskAPIView.as_view({'get':'get'})),
    #path('task/new',taskAPIView.as_view({'post':'post'})),
]