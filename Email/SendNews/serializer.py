from rest_framework import serializers
from .models import RegisterationNewuser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterationNewuser
        fields = ('id', 'username','email')