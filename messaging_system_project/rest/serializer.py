from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.contrib.auth.models import User
from .models import Message


# Serializers define the API representation.
class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# Serialized Message
class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'message', 'subject', 'creation_date', 'read']
