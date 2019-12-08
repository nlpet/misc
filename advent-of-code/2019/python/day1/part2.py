from math import floor


def main():
    with open('input.txt', 'r') as fr:
        masses = [int(n) for n in fr.readlines()]

    total_fuel, fuel = 0, 0

    for m in masses:
        fuel = m
        while True:
            fuel = floor(fuel / 3) - 2
            if fuel > 0:
                total_fuel += fuel
            else:
                break

    print('Answer to part 2: {}'.format(total_fuel))


if __name__ == '__main__':
    main()
