from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from ho_uz.place.models import Category, Place, PlaceShots, Services



class BaseAdmin:
    def tools_column(self, obj):
        if isinstance(obj, Category):
            view_obj = 'category'
        elif isinstance(obj, Place):
            view_obj = 'place'
        else:  # Product
            view_obj = 'place'
        hider_html_text = (
            '<a href="{hide_url}" class="btn btn-warning">Скрыть</a>' if obj.hide is False else
            '<a href="{active_url}" class="btn btn-success">Показать</a>'
        ).format(
            hide_url=reverse('api:actions:hide', args=[obj.pk, view_obj]),  # hide
            active_url=reverse('api:actions:activate', args=[obj.pk, view_obj]),  # activate
        )
        delete_html_text = '<a href="{0}" class="btn btn-danger">Удалить</a>'.format(
            reverse('api:actions:delete', args=[obj.pk, view_obj])  # delete
        )
        show_html_text = '<a href="{0}" class="btn btn-info">Посмотреть</a>'.format(
            reverse('api:actions:show', args=[obj.pk, view_obj])  # delete
        )
        html_tag = (
            '<a href="{0}" class="btn btn-secondary">Клонировать</a> '  # clone
        ).format(reverse('api:actions:clone', args=[obj.pk, view_obj]))
        html_text = hider_html_text + html_tag + show_html_text + delete_html_text
        return mark_safe(html_text)

    tools_column.short_description = 'Инструменты'
    tools_column.allow_tags = True

    def image_preview(self, obj):
        return mark_safe(
            f'<img src="{obj.photo.url}" width="200"/>'  # if obj.image else '<div>Rasmsiz</div>'
        )

    image_preview.short_description = 'Фото'
    image_preview.allow_tags = True


class PlaceShotsInline(admin.TabularInline):
    model = PlaceShots
    extra = 0


@admin.register(Category)
class CategoryAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = ['name', 'tools_column']


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    ...


@admin.register(Place)
class PlaceAdmin(BaseAdmin, admin.ModelAdmin):
    inlines = [PlaceShotsInline]
    list_display = ['name', 'image_preview', 'category', 'tools_column']
