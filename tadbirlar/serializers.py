from rest_framework import serializers
from tadbirlar.models import Kanferensiyalar, Seminarlar, Yangiliklar


class KanferensiyalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanferensiyalar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.kanferensiya_images.all()
        print(images)

        if images:
            data['images'] = [{'image': img.image.url} for img in images]

        return data


class SeminarlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminarlar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.seminar_images.all()
        print(images)

        if images:
            data['images'] = [{'image': img.image.url} for img in images]

        return data


class YangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.yangilik_images.all()
        print(images)

        if images:
            data['images'] = [{'image': img.image.url} for img in images]

        return data
