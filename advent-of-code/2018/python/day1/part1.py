def main():
    with open('input.txt', 'r') as fr:
        answer = sum([int(n) for n in fr.readlines()])
    print('Answer to part 1: {}'.format(answer))


if __name__ == '__main__':
    main()
