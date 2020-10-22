from django.contrib import admin
from django.urls import path, re_path
from rest.views import (
    MessagesDetailApiView,
    UserViewSet,
    UpdateMessageModelView,
    CreateMessageModelView,
    MessageDetailApiView,
    DeleteMessageModelView)
from rest_framework import routers, serializers
from django.conf.urls import include, url

# Routers provide an easy way of aroutersutomatically determining the URL conf.
router = routers.DefaultRouter()

router.register('users', UserViewSet)
#router.register('messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', CreateMessageModelView.as_view(), name='create'),
    re_path(r'^(?P<pk>[\w-]+)/update/$', UpdateMessageModelView.as_view(), name='update'),
    re_path(r'^(?P<pk>[\w-]+)/delete/$', DeleteMessageModelView.as_view(), name='delete'),
    re_path(r'^message/$', MessageDetailApiView.as_view(), name='message'),
    re_path(r'^messages/$', MessagesDetailApiView.as_view(), name='messages'),
]