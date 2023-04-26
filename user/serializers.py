from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'name'

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = 'score','user','game_code'