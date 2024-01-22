from rest_framework import serializers

from matbuotlar.models import Matbuotlar, Matbuot_categoriya


class Matbuot_categoriyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matbuot_categoriya
        fields = ('id', 'title',)


class MatbuotlarSerializer(serializers.ModelSerializer):
    categoriya = serializers.SerializerMethodField()

    class Meta:
        model = Matbuotlar
        fields = ('id', 'title', 'image', 'file', 'categoriya',)

    #
    def get_categoriya(self, obj):
        print(obj)
        return obj.categoriya.title if obj.categoriya else None
