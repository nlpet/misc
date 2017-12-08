# --- Day 1: Inverse Captcha ---


def read_input(filename: str) -> str:
    with open(filename, 'r') as fr:
        return fr.read().strip()


def main() -> None:
    seq = read_input('input.txt')
    seq += seq[0]
    total = 0

    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            total += int(seq[i - 1])

    print(total)


if __name__ == '__main__':
    main()
