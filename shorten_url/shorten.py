from shorten_url.models import Url
from django.shortcuts import get_object_or_404
import hashlib


def shorten_url(original_url):
    base62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    md5_hash = hashlib.md5()
    md5_hash.update(original_url.encode('utf-8'))
    md5_hash = md5_hash.hexdigest()

    str_in = md5_hash
    while len(str_in) > 8:

        int_hash = ""
        for c in str_in:
            if c.isalpha():
                int_hash += str(ord(c) % 10)
            else:
                int_hash += c

        str_out = ""
        sum = int(int_hash)
        while sum >= 62:
            str_out += base62[sum % 62]
            sum //= 62
        str_out += base62[sum]
        str_in = str_out

    shortened_url = str_in
    return Url(original_url=original_url, shortened_url=shortened_url)


def get_original_url(shortened_url):
    url = get_object_or_404(Url, shortened_url=shortened_url)
    return url.original_url
