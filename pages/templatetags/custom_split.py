from django import template

register = template.Library()

# @register.filter(name='custom_split')
@register.filter
def custom_split(value, arg):
    """
    Splits the value by a given string (arg).
    """
    return value.split(arg)
