from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from urlshortener import views

router = DefaultRouter()
router.register('url-shorteners', views.UrlShortenerViewSet)

urlpatterns = [
    re_path(r'^api/v1/', include(router.urls)),
    re_path(r'^api/v1/url-shorteners/short-url/(?P<short_url>.+)/',
            views.UrlShortenerViewSet.as_view({'get': 'get_shorten_url'}),
            name='get_shorten_url'),
]
