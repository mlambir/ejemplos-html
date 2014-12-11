from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.
from django.template import RequestContext
from main.models import Element, Example


def index(request):

    return render_to_response('index.html',
                              {"elements": Element.objects.all()},
                              context_instance=RequestContext(request))

def element(request, id):
    return render_to_response('element.html',
                              {"element": get_object_or_404(Element, pk=id)},
                              context_instance=RequestContext(request))

def example(request, id):
    return render_to_response('example.html',
                              {"example": get_object_or_404(Example, pk=id)},
                              context_instance=RequestContext(request))
