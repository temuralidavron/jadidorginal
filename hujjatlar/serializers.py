from rest_framework import serializers
from .models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Hikmatlar, Arxiv_hujjatlar, Dissertatsiya



class AsarlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asarlar
        fields = '__all__'


class MaqolalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqolalar
        fields = '__all__'


class TadqiqotlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tadqiqotlar
        fields = '__all__'


class SherlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sherlar
        fields = '__all__'


class HotiralarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotiralar
        fields = '__all__'


class HikmatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hikmatlar
        fields = '__all__'


class Arxiv_hujjatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arxiv_hujjatlar
        fields = '__all__'


class DissertatsiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dissertatsiya
        fields = '__all__'
