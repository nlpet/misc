import pydash


def get_key(lst):
    return ".".join([f.replace(".", "\.") for f in lst])


def construct_file_tree(output):
    tree = {"size": 0}
    idx, l = 0, len(output)
    loc, order = [], []

    while idx < l:
        out = output[idx]
        if out.startswith("$"):
            cmd = out.split(" ")[1:]
            if cmd[0] == "ls":
                pass
            elif cmd[0] == "cd":
                d = cmd[1]
                if d == "/":
                    loc = []
                elif d == "..":
                    loc.pop()
                else:
                    loc.append(d.replace(".", "\."))
        else:
            a, b = out.split(" ")
            key = get_key(loc + [b])
            order.append(loc + [b])
            if out.startswith("dir"):
                pydash.set_(tree, key, {"size": 0, "type": "directory"})
            else:
                pydash.set_(tree, key, {"size": int(a), "type": "file"})
        idx += 1
    return tree, order


def update_sizes(tree, stack):
    while stack:
        loc = stack.pop()
        key = get_key(loc)
        size = pydash.get(tree, key)["size"]
        parent_size_key = get_key(loc[:-1] + ["size"])
        parent_size = pydash.get(tree, parent_size_key)
        pydash.set_(tree, parent_size_key, parent_size + size)


def solve():
    with open("input.txt") as fr:
        output = [line.strip() for line in fr.readlines()]

    tree, order = construct_file_tree(output)
    update_sizes(tree, order[:])

    total_disk_space = 70000000
    unused_disk_space_needed = 30000000
    unused_disk_space = total_disk_space - tree["size"]
    to_delete = unused_disk_space_needed - unused_disk_space

    sizes = [tree["size"]]
    stack = order[:]

    while stack:
        loc = stack.pop()
        key = get_key(loc)
        file = pydash.get(tree, key)
        if file["type"] == "directory" and file["size"] >= to_delete:
            sizes.append(file["size"])

    print(min(sizes))


if __name__ == "__main__":
    solve()
