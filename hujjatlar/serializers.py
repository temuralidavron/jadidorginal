from rest_framework import serializers
from .models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Hikmatlar, Arxiv_hujjatlar, Dissertatsiya


class AsarlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asarlar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            data['files'] = [{'file': img.file.url} for img in files]

        return data


class MaqolalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqolalar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            data['files'] = [{'file': img.file.url} for img in files]

        return data


class TadqiqotlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tadqiqotlar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            data['files'] = [{'file': img.file.url} for img in files]

        return data


class SherlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sherlar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            data['files'] = [{'file': img.file.url} for img in files]

        return data


class HotiralarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotiralar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            data['files'] = [{'file': img.file.url} for img in files]

        return data


class HikmatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hikmatlar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            data['files'] = [{'file': img.file.url} for img in files]

        return data


class Arxiv_hujjatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arxiv_hujjatlar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            data['files'] = [{'file': img.file.url} for img in files]

        return data


class DissertatsiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dissertatsiya
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            data['files'] = [{'file': img.file.url} for img in files]

        return data

