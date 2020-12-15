def main():

    goal = 2020
    starting = "2,1,10,11,0,6"
    numbers = [int(n) for n in starting.split(",")]

    lookup = {}

    for i, n in enumerate(numbers):
        lookup[n] = [None, i + 1]

    last_number = numbers[-1]

    for turn in range(len(numbers) + 1, goal + 1):
        seen = lookup[last_number]

        if seen[0] is None:
            last_number = 0
        else:
            last_number = seen[1] - seen[0]

        seen = lookup.get(last_number, [None])
        lookup[last_number] = [seen[-1], turn]

    print(last_number)


if __name__ == "__main__":
    main()
