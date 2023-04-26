from rest_framework import serializers
from .models import *

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = 'id','username','word','score'

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = 'word','score_value'