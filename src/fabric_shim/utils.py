# Auxiliary tools

def enum_type(*sequential, **named) -> type:
    """enum other than class Enum. better performance

    Typical usage example:
        >> Numbers = enum('ZERO', 'ONE', 'TWO')
        >> Numbers.ZERO
        0
    or:
        >> Numbers = enum_type(ONE=1, TWO=2, THREE='three')
        >> Numbers.THREE
        'three'
    Args:
        sequential: Collects all the positional arguments in a tuple.
        named: Collects all the keyword arguments in a dictionary.

    """
    print(sequential, ": ", named)
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

class ResponseCode:
    OK = 200,
    ERROR_THRESHOLD = 400,
    ERROR = 500

MIN_UNICODE_RUNE_VALUE = '\u0000'
MAX_UNICODE_RUNE_VALUE = '\u{10ffff}'
COMPOSITEKEY_NS = '\x00'
EMPTY_KEY_SUBSTITUTE = '\x01'

def validate_composite_key_attribute(attr):
    if attr is None or not isinstance(attr, str) or len(attr) == 0:
        raise Exception('object type or attribute not a non-zero length string')

def validate_simple_keys(keys):
    for key in keys:
        if key and isinstance(key, str) and key[0] == COMPOSITEKEY_NS:
            raise Exception('first character of the key %s contains a null character which is not allowed' % key)
