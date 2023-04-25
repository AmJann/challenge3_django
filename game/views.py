from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import UserSearlizer
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

class TopScoresView(APIView):
    def get(self, request):
        top_scores = Player.objects.order_by('-score')[:5]
        serializer = PlayerSerializer(top_scores, many=True)
        return Response(serializer.data)

