# --- Day 6: Signals and Noise ---

from collections import Counter
import numpy as np


def main() -> None:
    with open('input.txt', 'r') as fr:
        messages = np.array([
            [ch for ch in msg.strip()] for msg in fr.readlines()]).T

    error_corrected_msg = []
    original_msg = []

    for msg in messages:
        most_common = Counter(msg).most_common()
        error_corrected_msg.append(most_common[0][0][0])
        original_msg.append(most_common[-1][0][0])

    print(('Error-corrected version of the message: '
           '{}'.format(''.join(error_corrected_msg))))
    print('Original message: {}'.format(''.join(original_msg)))


if __name__ == '__main__':
    main()
