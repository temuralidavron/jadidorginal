from rest_framework import serializers
from hikmatli_sozlar.models import Hikmatli_sozlar


class Hikmatli_sozlarSerializer(serializers.ModelSerializer):
    jadid_fullname = serializers.SerializerMethodField()
    class Meta:
        model = Hikmatli_sozlar
        fields = ('id', 'jadid_fullname', 'jadid', 'text', 'create', 'update',)

    def get_jadid_fullname(self, obj):
        return obj.jadid.fullname if obj.jadid else None


