from django.urls import path
from .views import SlayderListCreateView#, SlayderDetailView

urlpatterns = [
    path('api/slayder/', SlayderListCreateView.as_view(), name='slayder-list-create'),
    # path('api/slayder/<int:pk>/', SlayderDetailView.as_view(), name='slayder-detail'),
]
