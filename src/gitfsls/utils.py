
from . import low_level_api


def autofind(obj):
    possibilities = []
    objs = low_level_api.find_all_objects()

    for o in objs:
        if o.startswith(obj):
            possibilities.append(o)

    if len(possibilities) == 1:
        return possibilities[0]

    return obj

