from django import template

register = template.Library()

@register.filter(name='format_number_with_commas')
def format_number_with_commas(number):
    return "{:,}".format(number)

@register.filter(name='convert_duration')
def convert_duration(time):
    min = time // 60
    sec = time % 60
    if sec < 10: sec = "0" + str(sec)
    return f"{min}:{sec}"
