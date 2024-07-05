from rest_framework import serializers
from .models import Place, Category, PlaceShots, Services


class PlaceShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceShots
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField(source="category.name", read_only=True)

    class Meta:
        model = Place
        fields = ["id", "category", "name", "photo", "category_name"]


class DetailPlaceSerializer(serializers.ModelSerializer):
    shots = PlaceShotsSerializer(many=True, read_only=True)
    services = ServicesSerializer(many=True, allow_empty=True)

    class Meta:
        model = Place
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
