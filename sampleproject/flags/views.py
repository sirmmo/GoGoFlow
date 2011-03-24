from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def test(request, template='hello.html'):
    '''
    render the django-flags test page.

    Optional parameters:

    template
        template file (default 'hello.html')
    '''
    return render_to_response(template,
                              {'flags_url':settings.FLAGS_URL},
                              context_instance=RequestContext(request))