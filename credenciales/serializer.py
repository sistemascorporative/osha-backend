from rest_framework import serializers
from .models import *
from datetime import datetime


class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificado
        fields = '__all__'


class DiplomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diploma
        fields = '__all__'


class CarnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carnet
        fields = '__all__'