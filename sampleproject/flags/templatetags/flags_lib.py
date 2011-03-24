from django.template import Library
from django.conf import settings

import flags.loaders.app_directories
import flags.loaders.filesystem

register = Library()

def flags_form(context):
    '''
    This will insert a form made of a list of flags.

    The template *flags/flags_form.html* is used for rendering.
    
    Usage::

        {% flags_form %}

    template loaders (optional): use these with language-dependant
    templates with path *templates/[LANGUAGE]/\*.html*  ::

        # Put the  flag loaders before standard loaders.
        # Templates will be searched in the templates/[LANGUAGE]
        # directories.
        TEMPLATE_LOADERS = (
            'flags.loaders.filesystem.load_template_source',
            'flags.loaders.app_directories.load_template_source',
            ...
        )

    middleware::

        # LocaleMiddleware must follow SessionMiddleware
        MIDDLEWARE_CLASSES = (
            ...
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.locale.LocaleMiddleware',
            ...
        )

    other settings::

        USE_I18N = True
        ...
        # the FLAGS_I18N_PREFIX parameter must match urls.py item:
        # urls.py     > (r'^PREFIX/i18n/', include('django.conf.urls.i18n')),
        # settings.py > FLAGS_I18N_PREFIX = '/PREFIX/i18n/'
        FLAGS_I18N_PREFIX = '/lang/i18n/'
        # flags served by local server
        FLAGS_URL = MEDIA_URL
        # flags served by net server
        #FLAGS_URL = 'http://djangodev.free.fr/flags/'
        
        # languages
        ugettext = lambda s: s
        LANGUAGES = (
            ('ar', ugettext('Arabic')),
            ('fr', ugettext('French')),
            ('en', ugettext('English')),
            ('es', ugettext('Spanish')),
            ('de', ugettext('German')),
            ('pl', ugettext('Polish')),
        )
    '''
    code = context['LANGUAGE_CODE']
    flags.loaders.app_directories.current_lang = code
    flags.loaders.filesystem.current_lang = code
    
    return {'i18n_prefix':settings.FLAGS_I18N_PREFIX,
            'LANGUAGES': context['LANGUAGES'],
            'flags_url': settings.FLAGS_URL,
            'redirect':None
            }
flags_form = register.inclusion_tag("flags/flags_form.html", takes_context=True)(flags_form)
