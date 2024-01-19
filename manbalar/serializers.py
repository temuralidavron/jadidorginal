from rest_framework import serializers
from manbalar.models import Videolar, Rasmlar, Audiolar


class VideolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videolar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        videos = instance.video_files.all()

        if videos:
            data['videos'] = [{'video': img.video.url} for img in videos]

        return data


class RasmlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasmlar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.rasimlar.all()
        print(images)

        if images:
            data['images'] = [{'image': img.image.url} for img in images]

        return data


class AudiolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiolar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        audios = instance.audio_files.all()
        print(audios)

        if audios:
            data['audios'] = [{'audio': img.audio.url} for img in audios]

        return data
