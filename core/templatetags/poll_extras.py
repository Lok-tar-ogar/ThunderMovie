from django import template

register = template.Library()



@register.filter(name="Brflen")
def Brflen(value, arg):
    return value[:arg] + '...' if len(value) > 10 else value[:arg]

@register.filter(name="split_movie")
def split_movie(value):
    return value.split(' ')