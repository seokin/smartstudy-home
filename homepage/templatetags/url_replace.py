# from http://stackoverflow.com/a/17068299/366908
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, field, value):
    dict_ = context['request'].GET.copy()
    dict_[field] = value
    return dict_.urlencode()
