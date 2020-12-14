import functools, operator

product = lambda n: functools.reduce(operator.mul, n)


def chinese_remainder(n, a):
    s = 0
    mul = product(n)
    for n_i, a_i in zip(n, a):
        p = mul // n_i
        s += a_i * mul_inv(p, n_i) * p
    return s % mul


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def main():
    with open("input.txt", "r") as fr:
        contents = fr.readlines()
        buses = contents[1].strip().split(",")

    buses = [(idx, int(bus)) for idx, bus in enumerate(buses) if bus != "x"]
    offsets, n = zip(*buses)
    p = product(n)
    remainder = chinese_remainder(n, offsets)
    print(p - remainder)


if __name__ == "__main__":
    main()
