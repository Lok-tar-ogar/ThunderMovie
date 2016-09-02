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
    try:
        return '<li class="list-group-item">百度网盘全集<a href='+value[0]+' target="_blank" >'+value[0]+'</a>'+value[1]+'</li>' if 'http://pan.' in value[0] else '<li class="list-group-item"><a href='+value[0]+' target="_blank" >'+value[1]+'</a></li>'
    except:
        return ''

@register.filter(name="ispwdtv")
def ispwd(value):
    try:
        return '<li class="list-group-item">百度网盘全集<a href='+value[0]+' target="_blank" >'+value[0]+'</a>'+value[1]+'</li>' if 'http://pan.' in value[0] else '<li class="list-group-item"><a href='+value[0]+' target="_blank" >'+value[1]+'</a></li>'
    except:
        return ''