from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from matbuotlar.models import Matbuotlar
from matbuotlar.serializers import MatbuotlarSerializer

from rest_framework.decorators import api_view
from rest_framework import filters


class MatbuotlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = MatbuotlarSerializer
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
            return Matbuotlar.objects.filter(type=type_param)
        else:
            return Matbuotlar.objects.all()


@api_view(['GET'])
def matbuotlardetail(request, pk):
    matbuotlar = get_object_or_404(Matbuotlar, pk=pk)
    serializer = MatbuotlarSerializer(matbuotlar, context={'request': request})
    return Response(serializer.data)
