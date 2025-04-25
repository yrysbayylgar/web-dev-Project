from django.urls import path
from .views import ShoeViewSet, ClothingViewSet

urlpatterns = [
    path('shoes/', ShoeViewSet.as_view(), name='shoes-list'),
    path('cloth/', ClothingViewSet.as_view(), name='cloth-list'),
]
