from django import template

register = template.Library()


@register.filter('startswith')
def startswith(text, starts):
    startlen = len(starts)
    if str(text)[:startlen] == str(starts):
        return True
    return False

@register.filter('strtype')
def strtype(text):
    return str(text)