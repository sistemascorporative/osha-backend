from rest_framework import serializers
from .models import *

# Define los serializers para cada modelo

class CredencialSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Credencial
        fields = [
            "crecod",
            "creestcod",
            "creprocod",
        ]


class CertificadoSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Certificado
        fields = [
            "cercod",
            "cerfecemi",
            "cerfeccad",
            "cersrc",
            "cercrecod",
            "cerestregcod",
        ]


class DiplomaSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Diploma
        fields = [
            "dipcod",
            "dipfecemi",
            "dipfeccad",
            "dipsrc",
            "dipcrecod",
            "dipestregcod",
        ]


class CarnetSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Carnet
        fields = [
            "carcod",
            "carsrc",
            "carcrecod",
            "carestregcod",
        ]