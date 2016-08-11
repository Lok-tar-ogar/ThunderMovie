from django import template

register = template.Library()



@register.filter(name="Brflen")
def Brflen(value, arg):
    return value[:arg] + '...' if len(value) > 10 else value[:arg]