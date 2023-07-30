from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

import httpagentparser

@require_http_methods(['GET'])
def get_download(request, *args, **kwargs):
    s = request.META['HTTP_USER_AGENT']
    parse = httpagentparser.detect(s)
    bot = parse['bot']
    if bot:
        raise HttpResponseNotFound()
    try:
        if kwargs['ware']:
            ware = kwargs['ware']
            browser = parse['browser']['name']
            if ware == "node":
                return redirect("https://github.com/signum-network/signum-node/releases")
            elif ware == "xt":
                if 'Chrom' in browser:
                    return redirect("https://chrome.google.com/webstore/detail/signum-xt-wallet/kdgponmicjmjiejhifbjgembdcaclcib")
                elif 'Firefox' in browser:
                    return redirect("https://addons.mozilla.org/en-US/firefox/addon/signum-xt-wallet/")
                else:
                    return redirect("https://github.com/signum-network/signum-xt-wallet/")
            else: 
                raise Exception("Not Found")
    except Exception as e:
        return HttpResponseNotFound(f"{e}")