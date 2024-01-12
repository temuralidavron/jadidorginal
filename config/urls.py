"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foydali_havolalar/', include('foydali_havolalar.urls')),
    path('hikmatli_sozlar/', include('hikmatli_sozlar.urls')),
    path('hujjatlar/', include('hujjatlar.urls')),
    path('ishtirokchilar/', include('ishtirokchilar.urls')),
    path('jadidlar/', include('jadidlar.urls')),
    path('manbalar/', include('manbalar.urls')),
    path('slayder/', include('slayder.urls')),
    path('tadbirlar/', include('tadbirlar.urls')),
    path('sahifalar/', include('sahifalar.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)