from math import floor


def main():
    with open('input.txt', 'r') as fr:
        answer = sum([floor(int(n) / 3) - 2 for n in fr.readlines()])
    print('Answer to part 1: {}'.format(answer))


if __name__ == '__main__':
    main()
