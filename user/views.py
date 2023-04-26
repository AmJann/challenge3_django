from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import *

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CheckUser(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(name=self.kwargs['name'])
        return queryset

class addScore(generics.CreateAPIView):
    queryset = Score.objects.all()
    searlizer_class = ScoreSerializer



class TopScoresView(generics.ListAPIView):
    def get(self, request):
        num_records = int(request.get_param.get('num_records',100))
        queryset = Score.obects.order_by('-score')[:num_records]
        serializer = ScoreSerializer(queryset, many=True)
        return Response(serializer.data)


class getScorebyGameId(generics.ListAPIView):
    def get(self, request):
        gameCode = request.get_params.get('gameCode', None)
        num_records = request.get_param.get('num_records',100)

        if num_records.lower() == 'all':
            queryset = Score.obects.filter(game_code = gameCode).order_by('-score')
        else:
            queryset = Score.obects.filter(game_code = gameCode).order_by('-score')[:num_records]


        serializer = ScoreSerializer(queryset, many=True)
        return Response(serializer.data)

