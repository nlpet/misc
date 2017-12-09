# --- Day 5: How About a Nice Game of Chess? ---

import hashlib
from typing import List
from random import randint


def main() -> None:
    input = 'ugkcyxxp'
    i = 0
    filled_in = 0
    password1: List[str] = []
    password2: List[str] = ['-1' for _ in range(8)]
    allowed = {'0', '1', '2', '3', '4', '5', '6', '7'}

    animation = """
       __
      /o \_____
      \__/-="="`

    """

    print(animation)

    while filled_in < 8:
        hash = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            pos, char = hash[5], hash[6]
            if len(password1) < 8:
                password1.append(pos)
            if pos in allowed and password2[int(pos)] == '-1':
                password2[int(pos)] = char
                filled_in += 1
        i += 1

    print('The first password is {}'.format(''.join(password1)))
    print('The second password is {}'.format(''.join(password2)))


if __name__ == '__main__':
    main()
