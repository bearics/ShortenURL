from shorten_url.models import Url


def shorten_url(original_url):
    shortened_url = original_url[0:4]
    return Url(original_url=original_url, shortened_url=shortened_url)
