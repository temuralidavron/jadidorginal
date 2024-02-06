from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from hujjatlar.models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Arxiv_hujjatlar, \
    Dissertatsiya
from hujjatlar.serializers import AsarlarSerializer, MaqolalarSerializer, TadqiqotlarSerializer, SherlarSerializer, \
    HotiralarSerializer, Arxiv_hujjatlarSerializer, DissertatsiyaSerializer

from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import filters


class AsarlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = AsarlarSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jadid__id', "turkiston_muxtoriyati", "til_va_imlo", "tadqiqotlar"]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Asarlar.objects.all()


@api_view(['GET'])
def asarlardetail(request, pk):
    asarlar = get_object_or_404(Asarlar, pk=pk)
    serializer = AsarlarSerializer(asarlar, context={'request': request})
    return Response(serializer.data)


class MaqolalarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = MaqolalarSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jadid__id', "turkiston_muxtoriyati", "til_va_imlo", "tadqiqotlar", "type",]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Maqolalar.objects.all()


@api_view(['GET'])
def maqolalardetail(request, pk):
    maqolalar = get_object_or_404(Maqolalar, pk=pk)
    serializer = MaqolalarSerializer(maqolalar, context={'request': request})
    return Response(serializer.data)


class TadqiqotlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = TadqiqotlarSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jadid__id', ]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('type', openapi.IN_QUERY, description='Filter by type', type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        type_param = self.request.query_params.get('type', None)
        if type_param:
            return Tadqiqotlar.objects.filter(type=type_param)
        else:
            return Tadqiqotlar.objects.all()


@api_view(['GET'])
def tadqiqotlardetail(request, pk):
    tadqiqotlar = get_object_or_404(Tadqiqotlar, pk=pk)
    serializer = TadqiqotlarSerializer(tadqiqotlar, context={'request': request})
    return Response(serializer.data)


class SherlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SherlarSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jadid__id', ]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('type', openapi.IN_QUERY, description='Filter by type', type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        type_param = self.request.query_params.get('type', None)
        if type_param:
            return Sherlar.objects.filter(type=type_param)
        else:
            return Sherlar.objects.all()


@api_view(['GET'])
def sherlardetail(request, pk):
    sherlar = get_object_or_404(Sherlar, pk=pk)
    serializer = SherlarSerializer(sherlar, context={'request': request})
    return Response(serializer.data)


class HotiralarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = HotiralarSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jadid__id', ]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('type', openapi.IN_QUERY, description='Filter by type', type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        type_param = self.request.query_params.get('type', None)
        if type_param:
            return Hotiralar.objects.filter(type=type_param)
        else:
            return Hotiralar.objects.all()


@api_view(['GET'])
def hotiralardetail(request, pk):
    hotiralar = get_object_or_404(Hotiralar, pk=pk)
    serializer = HotiralarSerializer(hotiralar, context={'request': request})
    return Response(serializer.data)


class Arxiv_hujjatlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Arxiv_hujjatlarSerializer
    pagination_class = ResultsSetPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('type', openapi.IN_QUERY, description='Filter by type', type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        type_param = self.request.query_params.get('type', None)
        if type_param:
            return Arxiv_hujjatlar.objects.filter(type=type_param)
        else:
            return Arxiv_hujjatlar.objects.all()


@api_view(['GET'])
def arxiv_hujjatlardetail(request, pk):
    arxiv_hujjatlar = get_object_or_404(Arxiv_hujjatlar, pk=pk)
    serializer = Arxiv_hujjatlarSerializer(arxiv_hujjatlar, context={'request': request})
    return Response(serializer.data)


class DissertatsiyaListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = DissertatsiyaSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Dissertatsiya.objects.all()


@api_view(['GET'])
def dissertatsiyadetail(request, pk):
    dissertatsiya = get_object_or_404(Dissertatsiya, pk=pk)
    serializer = DissertatsiyaSerializer(dissertatsiya, context={'request': request})
    return Response(serializer.data)
