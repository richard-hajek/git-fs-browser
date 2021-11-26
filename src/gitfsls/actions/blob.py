import sys

from .. import low_level_api
from . import a as obj_any


def command(args):

    if args.list:
        print(obj_any.format_obj_list(low_level_api.get_all_of_type("blob")))

    elif args.obj:

        if low_level_api.get_type(args.obj) != "blob":
            print("Failed! Object not a blob type", file=sys.stderr)
            return 1

        print(low_level_api.get_content(args.obj))

    return 0