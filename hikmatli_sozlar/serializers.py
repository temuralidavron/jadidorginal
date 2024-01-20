from rest_framework import serializers
from hikmatli_sozlar.models import Hikmatli_sozlar


class Hikmatli_sozlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hikmatli_sozlar
        fields = '__all__'
