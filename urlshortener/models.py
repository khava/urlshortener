from django.db import models


class UrlShortener(models.Model):
    """ Сокращенная ссылка """
    original_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True, blank=True)
    followed = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta """
        verbose_name = 'Сокращенная ссылка'
        verbose_name_plural = 'Сокращенные ссылки'

    def __str__(self):
        return f'{self.original_url}'
