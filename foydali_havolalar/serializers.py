from rest_framework import serializers
from foydali_havolalar.models import Foydali_havolalar

class Foydali_havolalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foydali_havolalar
        fields = '__all__'




