from rest_framework.serializers import ModelSerializer

from urlshortener import models


class UrlShortenerSerializer(ModelSerializer):
    class Meta:
        model = models.UrlShortener
        fields = ('original_url', 'short_url', 'followed', 'created_at',)

        read_only_fields = ('short_url', 'followed', 'created_at',)
