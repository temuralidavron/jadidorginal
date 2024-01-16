from rest_framework import serializers
from ishtirokchilar.models import Ishtirokchilar

class IshtirokchilarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ishtirokchilar
        fields = '__all__'
        # fields = ('fullname',)