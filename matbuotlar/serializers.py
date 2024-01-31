from rest_framework import serializers
from matbuotlar.models import Matbuotlar


class MatbuotlarSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Matbuotlar
        fields = ('id', 'title', 'image', 'file', 'type', 'count',)

    def get_type(self, obj):
        return obj.get_type_display()
