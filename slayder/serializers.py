from rest_framework import serializers
from slayder.models import Slayder


class SlayderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slayder
        fields = ('id', 'title', 'text', 'citations', 'image', 'create', 'update',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.slayder_images.all()
        print(images)

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        return data
