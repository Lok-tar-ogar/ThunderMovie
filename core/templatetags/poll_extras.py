from django import template

register = template.Library()



@register.filter(name="Brflen")
def Brflen(value, arg):
    return value[:arg] + '...' if len(value) > 10 else value[:arg]

@register.filter(name="split_movie")
def split_movie(value):
    return value.split(' ')


@register.filter(name="ispwd")
def ispwd(value):
    return value if '密码' in value else '<a href='+value+' target="_blank" class="list-group-item">'+value+'</a>'