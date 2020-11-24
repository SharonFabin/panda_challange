from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import HeroSerializer, UserSerializer, GroupSerializer, EventSerializer
from .models import Hero, Event


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('event_type')
    serializer_class = EventSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CountWords(ViewSet):
    def list(self, request, format=None):
        events = Event.objects.all()
        res = {}
        for event in events:
            if event.data in res:
                res[event.data] += 1
            else:
                res.update({event.data: 1})

        return Response(res)
