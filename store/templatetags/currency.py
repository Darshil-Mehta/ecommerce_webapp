from django import template

register = template.Library()

@register.filter(name='currency_converter')
def currency_converter(cost):
    return "₹. "+str(cost)