from django import template

register = template.Library()

@register.filter(name='format_number_with_commas')

def format_number_with_commas(number):
    return "{:,}".format(number)