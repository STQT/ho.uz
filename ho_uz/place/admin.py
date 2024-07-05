from django.contrib import admin

from ho_uz.place.models import Category, Place, PlaceShots, Services


class PlaceShotsInline(admin.TabularInline):
    model = PlaceShots
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    ...


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceShotsInline]
