from rest_framework import serializers
from jadidlar.models import Jadid


class JadidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jadid
        fields = '__all__'
