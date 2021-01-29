import six
from graphene.utils.str_converters import to_snake_case
from django.utils.functional import Promise


def isiterable(value):
    try:
        iter(value)
    except TypeError:
        return False
    return True


def snake_case(data):
    if isinstance(data, dict):
        return {to_snake_case(k): snake_case(v) for k, v in data.items()}
    if isiterable(data) and not isinstance(data, (six.string_types, Promise)):
        return [snake_case(d) for d in data]
    return data
