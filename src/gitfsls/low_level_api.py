import subprocess
from typing import List


def find_all_objects() -> List[str]:
    proc = subprocess.Popen(["find", ".git/objects", "-type", "f"], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    objects = [x.replace(".git/objects/", "").replace("/", "") for x in out.decode().split("\n")]
    objects = filter(None, objects)
    return list(objects)


def get_type(obj: str) -> str:
    proc = subprocess.Popen(f"git cat-file -t {obj}", stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out.decode().strip()


def get_content(obj: str) -> str:
    proc = subprocess.Popen(f"git cat-file -p {obj}", stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out.decode().strip()


def get_size(obj: str) -> int:
    proc = subprocess.Popen(f"git cat-file -s {obj}", stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return int(out.decode().strip())


def get_all_of_type(t: str) -> List[str]:
    objs = find_all_objects()
    blobs = [obj for obj in objs if get_type(obj) == t]
    return blobs
