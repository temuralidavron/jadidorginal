from urllib.parse import urljoin

from rest_framework.decorators import api_view
from rest_framework.response import Response

from slayder.models import Slayder
from tadbirlar.models import Yangiliklar
from jadidlar.models import Jadid
from hujjatlar.models import Asarlar, Maqolalar
from hikmatli_sozlar.models import Hikmatli_sozlar


def update_image_urls(objects, request, target_base_url):
    for obj in objects:
        if 'image' in obj and obj['image']:
            obj['image'] = urljoin(target_base_url, obj['image'])
    return objects

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

    return_data['slider'] = update_image_urls(objs_slider, request, 'https://jadidlar.pythonanywhere.com')
    return_data['yangi'] = update_image_urls(objs_yangi, request, 'https://jadidlar.pythonanywhere.com')
    return_data['jadid'] = update_image_urls(objs_jadid, request, 'https://jadidlar.pythonanywhere.com')
    return_data['asar'] = update_image_urls(objs_asar, request, 'https://jadidlar.pythonanywhere.com')
    return_data['hikmat'] = update_image_urls(objs_hikmat, request, 'https://jadidlar.pythonanywhere.com')
    return_data['maqola'] = update_image_urls(objs_maqola, request, 'https://jadidlar.pythonanywhere.com')

    return Response(data=return_data)

