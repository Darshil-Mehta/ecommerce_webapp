from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name='product_quantity')
def product_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='single_item_cost')
def single_item_cost(product, cart):
    return product.price * product_quantity(product, cart)

@register.filter(name='total_cart_cost')
def total_cart_cost(cartdata, cart):
    sum = 0
    for cd in cartdata:
        sum += single_item_cost(cd, cart)
    return sum

@register.filter(name='order_row_cost')
def order_row_cost(num1, num2):
    return num1 * num2

@register.filter(name='currency_converter')
def currency_converter(cost):
    return "₹. "+str(cost)