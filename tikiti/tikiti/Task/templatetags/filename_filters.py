from django import template
import os
register = template.Library()


@register.filter
def filename(value):
    if hasattr(value, 'name'):
        return os.path.basename(value.name)
    return os.path.basename(value)

