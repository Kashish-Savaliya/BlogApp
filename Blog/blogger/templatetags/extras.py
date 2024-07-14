# This file defines a custom template filter called get_val.
# This filter is intended to retrieve a value from a dictionary using a key.

from django import template

# Creating an instance of Django's template library.
register = template.Library()

# Registers a custom filter named get_val.
# This means in templates, you can use {{ some_dict|get_val:some_key }} to get the value associated with some_key in some_dict.
@register.filter(name='get_val')
def get_val(dict, key):
    return dict.get(key)