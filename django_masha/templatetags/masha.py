from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('masha/masha.html')
def masha():
    context = {'STATIC_URL': settings.STATIC_URL}

    if hasattr(settings, 'MASHA_CFG') and settings.MASHA_CFG:
        context['MASHA_CFG'] = str(settings.MASHA_CFG)

    if hasattr(settings, 'MASHA_JQUERY') and settings.MASHA_JQUERY:
        context['MASHA_JQUERY'] = True

    return context
