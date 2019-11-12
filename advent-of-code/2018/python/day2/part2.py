def main():
    seen, current, answer = set([0]), 0, None

    while True:
        with open('input.txt', 'r') as fr:
            for line in fr:
                current += int(line.strip())
                if current in seen:
                    answer = current
                    break
                else:
                    seen.add(current)

        if answer is not None:
            break

    print('Answer to part 2: {}'.format(answer))


if __name__ == '__main__':
    main()
