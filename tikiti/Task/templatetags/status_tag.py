# templatetags/task_extras.py
from django import template

register = template.Library()

@register.filter
def status_color(status):
    return {
        #'New': 'secondary',
        'Analysis': 'primary',
        'Working On It': 'info',
        'Deliver': 'success',
        'Closed': 'success',
        'Reopened': 'dark'
    }.get(status, 'secondary')
