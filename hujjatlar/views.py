from rest_framework import generics
from .models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Hikmatlar, Arxiv_hujjatlar, Dissertatsiya
from .serializers import AsarlarSerializer, MaqolalarSerializer, TadqiqotlarSerializer, \
    SherlarSerializer, HotiralarSerializer, HikmatlarSerializer, DissertatsiyaSerializer, Arxiv_hujjatlarSerializer


class AsarlarListCreateView(generics.ListAPIView):
    queryset = Asarlar.objects.all()
    serializer_class = AsarlarSerializer

# class AsarlarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Asarlar.objects.all()
#     serializer_class = AsarlarSerializer


class MaqolalarListCreateView(generics.ListAPIView):
    queryset = Maqolalar.objects.all()
    serializer_class = MaqolalarSerializer

# class MaqolalarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Maqolalar.objects.all()
#     serializer_class = MaqolalarSerializer


class TadqiqotlarListCreateView(generics.ListAPIView):
    queryset = Tadqiqotlar.objects.all()
    serializer_class = TadqiqotlarSerializer

# class TadqiqotlarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tadqiqotlar.objects.all()
#     serializer_class = TadqiqotlarSerializer


class SherlarListCreateView(generics.ListAPIView):
    queryset = Sherlar.objects.all()
    serializer_class = SherlarSerializer

# class SherlarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Sherlar.objects.all()
#     serializer_class = SherlarSerializer


class HotiralarListCreateView(generics.ListAPIView):
    queryset = Hotiralar.objects.all()
    serializer_class = HotiralarSerializer

# class HotiralarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Hotiralar.objects.all()
#     serializer_class = HotiralarSerializer


class HikmatlarListCreateView(generics.ListAPIView):
    queryset = Hikmatlar.objects.all()
    serializer_class = HikmatlarSerializer

# class HikmatlarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Hikmatlar.objects.all()
#     serializer_class = HikmatlarSerializer


class Arxiv_hujjatlarListCreateView(generics.ListAPIView):
    queryset = Arxiv_hujjatlar.objects.all()
    serializer_class = Arxiv_hujjatlarSerializer


# class Arxiv_hujjatlarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Arxiv_hujjatlar.objects.all()
#     serializer_class = Arxiv_hujjatlarSerializer


class DissertatsiyaListCreateView(generics.ListAPIView):
    queryset = Dissertatsiya.objects.all()
    serializer_class = DissertatsiyaSerializer

# class DissertatsiyaDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Dissertatsiya.objects.all()
#     serializer_class = DissertatsiyaSerializer