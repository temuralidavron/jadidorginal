from rest_framework import serializers
from sahifalar.models import Sahifalar

class SahifalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sahifalar
        fields = '__all__'




