from django.contrib import admin

from urlshortener.models import UrlShortener


@admin.register(UrlShortener)
class UrlShortenerAdmin(admin.ModelAdmin):
    pass

