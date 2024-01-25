from rest_framework.decorators import api_view
from rest_framework.response import Response

from slayder.models import Slayder
from tadbirlar.models import Yangiliklar
from jadidlar.models import Jadid
from hujjatlar.models import Asarlar, Maqolalar
from hikmatli_sozlar.models import Hikmatli_sozlar



@api_view(['GET'])
def full_text_search(request):
    data = request.GET.get('search', 'salom dunyo')

    return_data = {}
    objs_slider = Slayder.objects.filter(title__icontains=data).values()
    objs_yangi = Yangiliklar.objects.filter(title__icontains=data).values()
    objs_jadid = Jadid.objects.filter(fullname__icontains=data).values()
    objs_asar = Asarlar.objects.filter(title__icontains=data).values()
    objs_hikmat = Hikmatli_sozlar.objects.filter(text__icontains=data).values()
    objs_maqola = Maqolalar.objects.filter(title__icontains=data).values()

    return_data['slider'] = objs_slider
    return_data['yangi'] = objs_yangi
    return_data['jadid'] = objs_jadid
    return_data['asar'] = objs_asar
    return_data['hikmat'] = objs_hikmat
    return_data['maqola'] = objs_maqola

    return Response(data=return_data)