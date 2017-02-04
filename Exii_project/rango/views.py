from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext


#class HomePage(TemplateView):
#    template_name = 'index.html'
moo = "ello baddy"
def index(request, moo = moo):
    context = RequestContext(request)

    context_dict = {'GreetingMessage': moo}

    return render_to_response('rango/index.html', context_dict, context)
