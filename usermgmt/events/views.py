from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Event
from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer, UserSerializer, UserRegistrationSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'events': reverse('event-list', request=request, format=format),
        'register': reverse('user-registration', request=request, format=format)
    })

class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Event.objects.filter(author=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated,
                      IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Event.objects.filter(author=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer  

class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]      

    	