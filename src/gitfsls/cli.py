import os

if __name__ == "__main__":

    workdir = os.getcwd()

    module = os.path.join(__file__, "..", "..")
    module = os.path.abspath(module)

    while True:
        cmd = input(">")

        cmds = cmd.strip().split(" ")

        if len(cmds) == 0:
            continue

        if cmds[0] == "cd":
            os.chdir(cmds[1])
            continue

        if cmds[0] == "ls":
            print(os.listdir("."))
            continue

        if cmds[0] == "pwd":
            print(os.getcwd())
            continue

        wd = os.getcwd()
        os.chdir(module)
        os.system(f"python -m gitfsls.main {wd} {cmd}")
        os.chdir(wd)