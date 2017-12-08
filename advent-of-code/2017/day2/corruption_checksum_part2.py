
def read_input(filename: str):
    rows = []
    with open(filename, 'r') as fr:
        return [
            [int(n) for n in row.strip().split('\t')]
            for row in fr.readlines()
        ]


def get_evenly_divisible_result(row):
    for i in range(len(row) - 1):
        for j in range(i + 1, len(row)):
            div = row[i] / row[j] if row[i] > row[j] else row[j] / row[i]
            if div.is_integer():
                return int(div)


def main() -> None:
    inp = read_input('input.txt')
    total = 0

    for row in inp:
        total += get_evenly_divisible_result(row)

    print(total)


if __name__ == '__main__':
    main()
