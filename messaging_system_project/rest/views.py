from .models import Message
from .serializer import MessageSerializer, UserSerializer, CreateMessageSerializer
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.db.models import Q


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class MessagesDetailApiView(ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        receiver_id = self.request.GET.get('receiver', None)
        unread = self.request.GET.get('unread', False)
        query = Q()
        if receiver_id == self.request.user.id or self.request.user.id == 1 and receiver_id:
            query &= Q(receiver_id=receiver_id)
        else:
            query &= Q(receiver_id=self.request.user.id)   # Only the sender or the receiver can see the messages
            query |= Q(sender_id=self.request.user.id)

        if unread:  # Add read query
            query &= Q(read=False)

        queryset_list = Message.objects.filter(query)
        return queryset_list


class MessageDetailApiView(ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    queryset = []
    entry = True

    def get_queryset(self):
        query = Q()
        query &= Q(receiver_id=self.request.user.id)   # Only receiver can see the messages
        query &= Q(read=False)
        queryset_list = Message.objects.filter(query)[:1]  # Get the first unread message
        if self.entry:      # Update the message read to true
            self.queryset.append(queryset_list)
            if len(queryset_list) != 0:
                Message.objects.filter(pk__in=queryset_list).update(read=True)
            self.entry = False
        message = self.queryset[-1] if len(self.queryset) != 0 else None
        return message if message else queryset_list


# Create new message
class CreateMessageModelView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    permission_classes = [IsAdminUser]


# Update message
class UpdateMessageModelView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAdminUser]


# Delete message
class DeleteMessageModelView(DestroyAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        message_id = self.kwargs['pk']
        query = Q()
        query &= Q(receiver_id=self.request.user.id) | Q(sender_id=self.request.user.id)
        query &= Q(id=message_id)
        queryset = Message.objects.filter(query)
        return queryset





