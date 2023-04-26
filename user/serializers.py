from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(many=False, read_only = True, slug_field = 'id')
    user_name = serializers.CharField(source='user.name')
    class Meta:
        model = Score
        fields = '__all__'