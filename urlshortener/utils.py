from random import choice
from string import ascii_letters, digits

from django.conf import settings

AVAILABLE_CHARS = ascii_letters + digits


def create_unique_code(chars=AVAILABLE_CHARS):
    """ Создание уникального кода для короткой ссылки """
    return ''.join([choice(chars) for _ in range(settings.MAXIMUM_SHORT_URL_CHARS)])


def create_shorten_url(model_instance):
    """ Генерация короткой ссылки """
    unique_code = create_unique_code()

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=unique_code).exists():
        return create_shorten_url(model_instance)

    return unique_code
