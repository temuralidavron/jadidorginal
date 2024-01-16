from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from hujjatlar.models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Hikmatlar, Arxiv_hujjatlar, \
    Dissertatsiya
from hujjatlar.serializers import AsarlarSerializer, MaqolalarSerializer, TadqiqotlarSerializer, SherlarSerializer, \
    HotiralarSerializer, HikmatlarSerializer, Arxiv_hujjatlarSerializer, DissertatsiyaSerializer

from rest_framework.decorators import api_view


class AsarlarListView(ListAPIView):
    serializer_class = AsarlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Asarlar.objects.all()


@api_view(['GET'])
def asarlardetail(request, pk):
    asarlar = get_object_or_404(Asarlar, pk=pk)
    serializer = AsarlarSerializer(asarlar)
    return Response(serializer.data)


class MaqolalarListView(ListAPIView):
    serializer_class = MaqolalarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Maqolalar.objects.all()


@api_view(['GET'])
def maqolalardetail(request, pk):
    maqolalar = get_object_or_404(Maqolalar, pk=pk)
    serializer = MaqolalarSerializer(maqolalar)
    return Response(serializer.data)


class TadqiqotlarListView(ListAPIView):
    serializer_class = TadqiqotlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Tadqiqotlar.objects.all()


@api_view(['GET'])
def tadqiqotlardetail(request, pk):
    tadqiqotlar = get_object_or_404(Tadqiqotlar, pk=pk)
    serializer = TadqiqotlarSerializer(tadqiqotlar)
    return Response(serializer.data)


class SherlarListView(ListAPIView):
    serializer_class = SherlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Sherlar.objects.all()


@api_view(['GET'])
def sherlardetail(request, pk):
    sherlar = get_object_or_404(Sherlar, pk=pk)
    serializer = SherlarSerializer(sherlar)
    return Response(serializer.data)


class HotiralarListView(ListAPIView):
    serializer_class = HotiralarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Hotiralar.objects.all()


@api_view(['GET'])
def hotiralardetail(request, pk):
    hotiralar = get_object_or_404(Hotiralar, pk=pk)
    serializer = HotiralarSerializer(hotiralar)
    return Response(serializer.data)


class HikmatlarListView(ListAPIView):
    serializer_class = HikmatlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Hikmatlar.objects.all()


@api_view(['GET'])
def hikmatlardetail(request, pk):
    hikmatlar = get_object_or_404(Hikmatlar, pk=pk)
    serializer = HikmatlarSerializer(hikmatlar)
    return Response(serializer.data)


class Arxiv_hujjatlarListView(ListAPIView):
    serializer_class = Arxiv_hujjatlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Arxiv_hujjatlar.objects.all()


@api_view(['GET'])
def arxiv_hujjatlardetail(request, pk):
    arxiv_hujjatlar = get_object_or_404(Arxiv_hujjatlar, pk=pk)
    serializer = Arxiv_hujjatlarSerializer(arxiv_hujjatlar)
    return Response(serializer.data)


class DissertatsiyaListView(ListAPIView):
    serializer_class = DissertatsiyaSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Dissertatsiya.objects.all()


@api_view(['GET'])
def dissertatsiyadetail(request, pk):
    dissertatsiya = get_object_or_404(Dissertatsiya, pk=pk)
    serializer = DissertatsiyaSerializer(dissertatsiya)
    return Response(serializer.data)