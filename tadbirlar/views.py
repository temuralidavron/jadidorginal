from rest_framework import generics
from tadbirlar.models import Kanferensiyalar, Seminarlar, Yangiliklar
from tadbirlar.serializers import KanferensiyalarSerializer, SeminarlarSerializer, \
    YangiliklarSerializer


class KanferensiyalarListCreateView(generics.ListAPIView):
    queryset = Kanferensiyalar.objects.all()
    serializer_class = KanferensiyalarSerializer

# class KanferensiyalarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Kanferensiyalar.objects.all()
#     serializer_class = KanferensiyalarSerializer


class SeminarlarListCreateView(generics.ListAPIView):
    queryset = Seminarlar.objects.all()
    serializer_class = SeminarlarSerializer

# class SeminarlarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Seminarlar.objects.all()
#     serializer_class = SeminarlarSerializer


class YangiliklarListCreateView(generics.ListAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer

# class YangiliklarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Yangiliklar.objects.all()
#     serializer_class = YangiliklarSerializer