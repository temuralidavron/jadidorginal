from rest_framework import serializers
from foydali_havolalar.models import Foydali_havolalar


class Foydali_havolalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foydali_havolalar
        fields = ('id', 'title', 'link', 'logo_image',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.foydali_havola_images.all()
        print(images)

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        return data
