def hash(s):
    value = 0
    for ch in s:
        value += ord(ch)
        value *= 17
        value = value % 256
    return value


def solve():
    with open("input.txt") as fr:
        sequence = fr.read().strip().split(",")

    boxes = {}

    for seq in sequence:
        if seq.endswith("-"):
            label = seq[:-1]
            box_id = hash(label)
            if box_id in boxes:
                boxes[box_id] = [l for l in boxes[box_id] if l[0] != label]
                if len(boxes[box_id]) == 0:
                    del boxes[box_id]
        else:
            label, focal_length = seq.split("=")
            box_id = hash(label)
            if box_id not in boxes:
                boxes[box_id] = []

            if label in [l[0] for l in boxes[box_id]]:  # replace
                boxes[box_id] = [
                    (label, focal_length) if l[0] == label else l for l in boxes[box_id]
                ]
            else:
                boxes[box_id].append((label, focal_length))

    total_focusing_power = 0

    for box_id, labels in boxes.items():
        for i, (l, n) in enumerate(labels):
            total_focusing_power += (box_id + 1) * (i + 1) * int(n)

    print(total_focusing_power)


if __name__ == "__main__":
    solve()
