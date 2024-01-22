from rest_framework import serializers
from ishtirokchilar.models import Ishtirokchilar


class IshtirokchilarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ishtirokchilar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.ishtirokchi_images.all()
        print(images)

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        return data
