# --- Day 15: Dueling Generators ---

from time import time


def main() -> None:
    # Test A: 65, Test B: 8921
    A = 883
    B = 879
    mask = 2 ** 16 - 1
    factor_A = 16807
    factor_B = 48271
    divisor = 2147483647
    count = 0

    start = time()

    for i in range(40000000):
        A = (A * factor_A) % divisor
        B = (B * factor_B) % divisor
        count += 1 if A & mask == B & mask else 0

    print('The count is {}'.format(count))
    print('Finished in {:.2f}'.format(time() - start))


if __name__ == '__main__':
    main()
