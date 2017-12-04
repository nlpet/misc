
def main():
    num_valid = 0

    with open('input.txt', 'r') as fr:
        passwords = fr.readlines()

    for password in passwords:
        words = [w for w in password.strip().split(' ')]
        if len(words) == len(set(words)):
            num_valid += 1

    print(num_valid)


if __name__ == '__main__':
    main()
