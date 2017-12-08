# --- Day 5: A Maze of Twisty Trampolines, All Alike ---


def main():
    with open('input.txt', 'r') as fr:
        instructions = [int(n.strip()) for n in fr.readlines()]

    index = 0
    steps = 0

    while 0 <= index <= len(instructions) - 1:
        offset = instructions[index]
        instructions[index] += 1
        index += offset
        steps += 1

    print(steps)


if __name__ == '__main__':
    main()
