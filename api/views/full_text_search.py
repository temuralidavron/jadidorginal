from rest_framework.decorators import api_view
from rest_framework.response import Response

from slayder.models import Slayder
from tadbirlar.models import Yangiliklar


@api_view(['GET'])
def full_text_search(request):
    data = request.GET.get('search', 'salom dunyo')

    return_data = {}
    objs_slider = Slayder.objects.filter(title__icontains=data)
    objs_yangi = Yangiliklar.objects.filter(title__icontains=data)

    return_data['slider'] = objs_slider
    return_data['yangi'] = objs_yangi


    return Response(return_data)