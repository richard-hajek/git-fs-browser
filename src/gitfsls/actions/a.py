from typing import List

from .. import low_level_api


def get_all() -> List[str]:
    objs = low_level_api.find_all_objects()
    blobs = [obj for obj in objs if low_level_api.get_type(obj)]
    return blobs


def format_obj_list(objs):
    output = ""

    for i, obj in enumerate(objs):
        output += f"{obj}\t{low_level_api.get_size(obj)}\t{low_level_api.get_content(obj)[0:40]}\n"

    return output


def command(args):
    if args.list:
        print(format_obj_list(low_level_api.find_all_objects()))
    elif args.obj:
        print(low_level_api.get_content(args.obj))
    return 0