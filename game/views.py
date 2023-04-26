from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Player
from .models import Computer

class ComputerListCreate(generics.ListCreateAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

class ComputerViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

class PlayerListCreate(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer



