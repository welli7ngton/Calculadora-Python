import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def isValidNumber(string: str, valido=False):
    try:
        float(string)
        valido = True

    except ValueError:
        valido = False
    return valido


def isEmpty(string: str):
    return len(string) == 0
