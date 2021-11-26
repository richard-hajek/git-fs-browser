import os
import subprocess


def root_ls():
    proc = subprocess.Popen(["find", ".git/objects", "-type", "f"], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    objects = [x.replace(".git/objects/", "").replace("/", "") for x in out.decode().split("\n")]
    objects = filter(None, objects)
    return list(objects)


def ls_trees(tree_obj):
    lines = cat(tree_obj)
    ls = []

    for line in lines.split("\n"):
        line = line.split("\t")[0]
        if ' tree ' in line:
            ls.append(line.split(" ")[2])

    return ls


def ls_objs(tree_obj):
    lines = cat(tree_obj)
    ls = []

    for line in lines.split("\n"):
        if ' blob ' in line:
            ls.append(line.split(" ")[2])

    return ls


def autofind_obj(obj):
    possibilities = []
    objs = root_ls()

    for o in objs:
        if o.startswith(obj):
            possibilities.append(o)

    if len(possibilities) == 1:
        return possibilities[0]

    return obj


def what_is(obj):
    proc = subprocess.Popen(f"git cat-file -t {obj}", stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out.decode().strip()


def cat(obj):
    proc = subprocess.Popen(f"git cat-file -p {obj}", stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out.decode().strip()


def find(obj, prefix=""):
    for tree in ls_trees(obj):
        print(f"{prefix}/{obj}/")
        find(tree, prefix=f"{prefix}/{tree}")

    for obj in ls_objs(obj):
        print(f"{prefix}/{obj}")

def is_git():
    return ".git" in os.listdir("../..")


def main():

    while True:
        cmd = input("> ")
        cmd = cmd.strip().split(" ")

        if len(cmd) == 0:
            continue

        if cmd[0] == "cd":
            os.chdir(cmd[1])
            continue

        if cmd[0] == "ls":
            print(os.listdir("../.."))
            continue

        if cmd[0] == "pwd":
            print(os.getcwd())
            continue

        if cmd[0] == "root":
            if not is_git():
                print("Have to be in git repo root")
                continue

            for obj in root_ls():
                print(f"{obj}\t{what_is(obj)}")

        if cmd[0] == "cat":
            if not is_git():
                print("Have to be in git repo root")
                continue

            obj = autofind_obj(cmd[1])

            print(cat(obj))

        if cmd[0] == "find":
            obj = autofind_obj(cmd[1])
            find(obj)


if __name__ == '__main__':
    main()