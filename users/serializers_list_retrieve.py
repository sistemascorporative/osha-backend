from rest_framework import serializers
from .models import *

# Define los serializers para cada modelo

class EstudianteUserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = EstudianteUser
        fields = [
            "id",
            "email",
            "usernom",
            "userape",
            "userdocide",
            "usercodosh",
            "userpai",
            "userciu",
            "userdir",
        ]