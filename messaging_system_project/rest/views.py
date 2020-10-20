from .models import Message
from .serializer import MessageSerializer, UserSerializer
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from django.http.response import JsonResponse


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageSpecificUserList(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        receiver_id = self.kwargs['pk']
        return Message.objects.filter(sender_id=self.request.user.id, receiver_id=receiver_id)