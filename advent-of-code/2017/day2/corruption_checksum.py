
def read_input(filename: str):
    rows = []
    with open(filename, 'r') as fr:
        return [
            [int(n) for n in row.strip().split('\t')]
            for row in fr.readlines()
        ]


def main() -> None:
    inp = read_input('input.txt')
    row_checksums = [max(row) - min(row) for row in inp]
    print(sum(row_checksums))


if __name__ == '__main__':
    main()
