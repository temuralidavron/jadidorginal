from rest_framework import serializers
from jadidlar.models import Jadid


class JadidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jadid
        fields = ('id', 'fullname', 'image', 'bio', 'birthday', 'die_day', 'order',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.jadid_images.all()
        print(images)

        if images:
            data['images'] = [{'image': img.image.url} for img in images]

        return data
