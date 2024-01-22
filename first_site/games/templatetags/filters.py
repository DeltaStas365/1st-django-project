from django.template import Library



register = Library()
@register.filter(name="active_stars")
def active_stars(number):
    return range(int(number))
@register.filter(name="is_half")
def is_half(number):
    return number(int(number)) >= 0.5
@register.filter(name="disabled_stars")
def disabled_stars(number):
    return range(10-int(float(number) + 0.5))