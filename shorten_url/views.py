from django.template.context_processors import csrf
from django.template.loader import get_template

from django.shortcuts import render

from shorten_url.forms import SendUrlForm
from shorten_url.models import Url

from shorten_url.models import Url
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from shorten_url.shorten import *


def home(request):
    # if get original url, make short
    context = {}
    new_url = False
    if request.method == "POST":
        form_data = SendUrlForm(request.POST)

        if form_data.is_valid():  # get normal url
            url = shorten_url(form_data.cleaned_data['original_url'])
            url.save()
            context.update({'updated_url': url})

        new_url = True

    context.update({'new_url': new_url})

    # get original url
    context.update({'send_url_form': SendUrlForm()})
    context.update(csrf(request))

    # show url list
    template = get_template('home.html')

    page_data = Paginator(Url.objects.all(), 3)
    page = request.GET.get('page')
    try:
        urls = page_data.page(page)
    except PageNotAnInteger:
        urls = page_data.page(1)
    except EmptyPage:
        urls = page_data.page(page_data.num_pages)

    context.update({'url_list': urls,
                    'current_page': page,
                    'total_page': range(1, page_data.num_pages + 1),
                    })

    return HttpResponse(template.render(context, request))


def redirect(request, shortened_url):
    redirect_url = get_original_url(shortened_url)
    return HttpResponseRedirect(redirect_to=redirect_url)