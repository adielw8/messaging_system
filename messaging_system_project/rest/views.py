from .models import Message
from .serializer import MessageSerializer, UserSerializer
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.db.models import Q


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessagesDetailApiView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset_list = Message.objects.all()
        receiver_id = self.request.GET.get('receiver')
        if receiver_id:
            queryset_list = Message.objects.filter(Q(sender_id=self.request.user.id) | Q(receiver_id=receiver_id) & Q(read=False))
            # TODO
            # add update function
        return queryset_list


class MessageDetailApiView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset_list = Message.objects.all()
        receiver_id = self.request.GET.get('receiver')
        if receiver_id:
            queryset_list = Message.objects.filter(Q(sender_id=self.request.user.id) | Q(receiver_id=receiver_id) & Q(read=False))[:1]
            # TODO
            # add update function
        return queryset_list


class CreateMessageModelView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj


class UpdateMessageModelView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class DeleteMessageModelView(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer





