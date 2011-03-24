from django.template.loaders import filesystem
from django.utils.translation import get_language

def load_template_source(template_name, template_dirs=None):
    local_template_name = '%s/%s' % (get_language(), template_name)
    return filesystem.load_template_source(local_template_name, template_dirs)
load_template_source.is_usable = True
