from rest_framework import serializers
from .models import *

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = 'id','user','word','score_value'

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = 'word','score_value'