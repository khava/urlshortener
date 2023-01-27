from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

SchemaView = get_schema_view(
    openapi.Info(
        title='REST API',
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^swagger/$', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', SchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('urlshortener.urls')),
]
