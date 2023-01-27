from django.http import HttpResponseRedirect
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from urlshortener import models, serializers, utils


class UrlShortenerViewSet(ModelViewSet):
    """ UrlShortener endpoints """
    queryset = models.UrlShortener.objects.all()
    serializer_class = serializers.UrlShortenerSerializer
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        request_data = serializer.validated_data

        short_url = utils.create_shorten_url(models.UrlShortener())
        request_data['short_url'] = short_url

        url_shorten = models.UrlShortener.objects.create(**request_data)

        return Response(self.serializer_class(url_shorten).data, status=201)

    @action(detail=True, url_path='short-url/<str:short_url>/', url_name='get-shorten-url', methods=['get'])
    def get_shorten_url(self, request, short_url):
        """ Переход по короткой ссылке """
        try:
            url_shorten = models.UrlShortener.objects.get(short_url=short_url)
            url_shorten.followed += 1
            url_shorten.save()

            return HttpResponseRedirect(url_shorten.original_url)
        except Exception:
            raise NotFound({'detail': f'Redirect by short url <{short_url}> failed.'})
