from typing import List

from .. import low_level_api


def get_all() -> List[str]:
    objs = low_level_api.find_all_objects()
    blobs = [obj for obj in objs if low_level_api.get_type(obj) == "tag"]
    return blobs


def command(args):
    return 0