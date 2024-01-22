from rest_framework import serializers
from jadidlar.models import Jadid


class JadidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jadid
        fields = ('fullname', 'image', 'bio', 'birthday', 'die_day', 'order','id', )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.jadid_images.all()
        print(images)

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        return data
