from rest_framework import serializers
from .models import *

# Define los serializers para cada modelo


class UserSimpleSerializerList(serializers.ModelSerializer):
    class Meta:
        model = UserSimple
        fields = [
            "usernom",
            "userape",
            "userdocide",
            "usercodosh",
            "userpai",
            "userciu",
            "userdir",
        ]


class EstudianteUserSerializerList(serializers.ModelSerializer):
    usuario = UserSimpleSerializerList()
    class Meta:
        model = EstudianteUser
        fields = [
            "id",
            "usuario",
            "email",
        ]