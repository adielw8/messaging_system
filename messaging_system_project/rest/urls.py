from django.contrib import admin
from django.urls import path, re_path
from rest.views import (
    MessagesDetailApiView,
    UserViewSet,
    MessageViewSet,
    UpdateMessageModelView,
    CreateMessageModelView,
    MessageDetailApiView,
    DeleteMessageModelView)
from rest_framework import routers, serializers
from django.conf.urls import include, url

# Routers provide an easy way of aroutersutomatically determining the URL conf.
router = routers.DefaultRouter()

# Routers provide an easy way of aroutersutomatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', CreateMessageModelView.as_view(), name='create'),
    url(r'^(?P<pk>[\w-]+)/update/$', UpdateMessageModelView.as_view(), name='update'),
    url(r'^(?P<pk>[\w-]+)/delete/$', DeleteMessageModelView.as_view(), name='delete'),
    url(r'^(?P<receiver>[\w-]+)/message/$', MessageDetailApiView.as_view(), name='message'),
    url(r'^(?P<receiver>[\w-]+)/messages/$', MessagesDetailApiView.as_view(), name='messages'),



]