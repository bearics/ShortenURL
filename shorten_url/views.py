from django.template.context_processors import csrf
from shorten_url.forms import SendUrlForm
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from shorten_url.shorten import *


def home(request):
    # if get original url, make short
    context = {}
    if request.method == "POST":
        form_data = SendUrlForm(request.POST)

        if form_data.is_valid():  # get normal url
            original_url = form_data.cleaned_data['original_url']
            if original_url.find("://") == -1:
                context.update({'error': '\"' + original_url + '\"' + ' is not url.'})
            else:
                if len(original_url) < 14:
                    context.update({'error': '\"' + original_url + '\"' + ' is too short.'})
                else:
                    url = shorten_url(original_url)
                    url.save()
                    context.update({'updated_url': url})

    # get original url
    context.update({'send_url_form': SendUrlForm()})
    context.update(csrf(request))

    # show url list
    urls = Url.objects.order_by('-date')

    context.update({'url_list': urls})

    return render(request, 'home.html', context)


def redirect(request, shortened_url):
    redirect_url = get_original_url(shortened_url)
    return HttpResponseRedirect(redirect_to=redirect_url)
