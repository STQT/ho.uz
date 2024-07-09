from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework import generics

from .serializers import PlaceSerializer, CategorySerializer, DetailPlaceSerializer
from .models import Place, Category

modelClass = {
    "place": Place,
    "category": Category
}


class PlaceListAPIView(generics.ListAPIView):
    queryset = Place.objects.select_related("category").filter(hide=False)
    serializer_class = PlaceSerializer
    filterset_fields = ["category_id"]


class PlaceDetailAPIView(generics.RetrieveAPIView):
    queryset = Place.objects.prefetch_related("shots")
    serializer_class = DetailPlaceSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all().filter(hide=False)
    serializer_class = CategorySerializer
    pagination_class = None  # Use default pagination settings from settings.py


def duplicate_product(request, product_id):
    product = get_object_or_404(Place, id=product_id)
    product.id = None
    product.save()
    return redirect(reverse('admin:place_place_changelist'))


def clone(request, pk, view_obj):
    obj = get_object_or_404(modelClass[view_obj], id=pk)
    obj.id = None
    obj.save()
    return redirect(reverse(f'admin:place_{view_obj}_changelist'))


def hide(request, pk, view_obj):
    obj = get_object_or_404(modelClass[view_obj], id=pk)
    obj.hide = True
    obj.save()
    return redirect(reverse(f'admin:place_{view_obj}_changelist'))


def activate(request, pk, view_obj):
    obj = get_object_or_404(modelClass[view_obj], id=pk)
    obj.hide = False
    obj.save()
    return redirect(reverse(f'admin:place_{view_obj}_changelist'))


def delete(request, pk, view_obj):
    obj = get_object_or_404(modelClass[view_obj], id=pk)
    obj.delete()
    return redirect(reverse(f'admin:place_{view_obj}_changelist'))


def preview_show(request, pk, view_obj):
    url_links = {
        "place": f"/{pk}"
    }
    return redirect("https://ho.uz" + url_links[view_obj])
