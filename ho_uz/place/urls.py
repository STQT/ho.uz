from django.urls import path
from .views import PlaceListAPIView, CategoryListAPIView, PlaceDetailAPIView

urlpatterns = [
    path('list/', PlaceListAPIView.as_view(), name='place-list'),
    path('detail/<int:pk>/', PlaceDetailAPIView.as_view(), name='place-detail'),
    path('categories/', CategoryListAPIView.as_view(), name='categories-list'),
]
