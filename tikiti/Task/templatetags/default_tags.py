from django import template
import os
register = template.Library()


@register.filter(name = "Default")
def DafaultFilter(value,arg):
          
    return value if value else arg

