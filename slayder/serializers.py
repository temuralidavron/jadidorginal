from rest_framework import serializers
from slayder.models import Slayder

class SlayderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slayder
        fields = '__all__'




