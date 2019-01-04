from shorten_url.models import Url
from django.shortcuts import get_object_or_404


def shorten_url(original_url):
    shortened_url = original_url[0:4]
    return Url(original_url=original_url, shortened_url=shortened_url)


def get_original_url(shortened_url):
    url = get_object_or_404(Url, shortened_url=shortened_url)
    return url.original_url
