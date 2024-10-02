from django.contrib import admin
from django.utils.html import format_html
from .models import Tourist


@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    search_fields = ('name', 'location')
    list_filter = ('name',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "이미지 없음"

    image_preview.short_description = '이미지 미리보기'

    readonly_fields = ('id', 'image_preview')

    fieldsets = (
        ('기본 정보', {
            'fields': ('name', 'location', 'description')
        }),
        ('이미지', {
            'fields': ('image', 'image_preview')
        }),
        ('운영 시간', {
            'fields': ('operating_hours',)
        }),
        ('입장료', {
            'fields': ('entrance_fee',)
        }),
        ('주차정보', {
            'fields': ('parking',)
        }),
    )
