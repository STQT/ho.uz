from django.urls import path
from .views import PlaceListAPIView, CategoryListAPIView, PlaceDetailAPIView, \
    hide, activate, clone, delete, preview_show

app_name = "actions"
urlpatterns = [
    path('hide/<int:pk>/<str:view_obj>/', hide, name='hide'),
    path('activate/<int:pk>/<str:view_obj>/', activate, name='activate'),
    path('clone/<int:pk>/<str:view_obj>/', clone, name='clone'),
    path('delete/<int:pk>/<str:view_obj>/', delete, name='delete'),
    path('show/<int:pk>/<str:view_obj>/', preview_show, name='show'),
    path('list/', PlaceListAPIView.as_view(), name='place-list'),
    path('detail/<int:pk>/', PlaceDetailAPIView.as_view(), name='place-detail'),
    path('categories/', CategoryListAPIView.as_view(), name='categories-list'),
]
