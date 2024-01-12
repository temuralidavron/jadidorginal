from rest_framework import generics
from jadidlar.models import Jadid
from jadidlar.serializers import JadidSerializer


class JadidListCreateView(generics.ListAPIView):
    queryset = Jadid.objects.all()
    serializer_class = JadidSerializer


# class JadidDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Jadid.objects.all()
#     serializer_class = JadidSerializer