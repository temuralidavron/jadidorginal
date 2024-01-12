from rest_framework import serializers
from manbalar.models import Videolar, Rasmlar, Audiolar


class VideolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videolar
        fields = '__all__'


class RasmlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasmlar
        fields = '__all__'


class AudiolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiolar
        fields = '__all__'