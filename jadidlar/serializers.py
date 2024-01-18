from rest_framework import serializers
from jadidlar.models import Jadid


class JadidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jadid
        fields = ('fullname', 'image', 'bio', 'birthday', 'die_day', 'order',)
