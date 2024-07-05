from rest_framework import generics
from .models import Place, Category
from .serializers import PlaceSerializer, CategorySerializer, DetailPlaceSerializer


class PlaceListAPIView(generics.ListAPIView):
    queryset = Place.objects.select_related("category")
    serializer_class = PlaceSerializer
    filterset_fields = ["category_id"]


class PlaceDetailAPIView(generics.RetrieveAPIView):
    queryset = Place.objects.prefetch_related("shots")
    serializer_class = DetailPlaceSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None  # Use default pagination settings from settings.py
