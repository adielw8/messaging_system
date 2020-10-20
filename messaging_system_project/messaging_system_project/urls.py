from django.contrib import admin
from django.urls import path, include
from rest.views import MessageViewSet, UserViewSet, MessageSpecificUserList
from django.contrib.auth.models import User
from rest_framework import routers, serializers





# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('messages', MessageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('users/messages/<int:pk>', MessageSpecificUserList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]