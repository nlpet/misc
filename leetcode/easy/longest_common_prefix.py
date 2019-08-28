def solution(words):
    root = dict()
    max_common, n_words = 0, len(words)
    for idx, word in enumerate(words):
        current_dict = root
        for idx, letter in enumerate(word):
            current_dict = current_dict.setdefault(letter, {})
            if current_dict.get('count'):
                current_dict['count'] += 1
            else:
                current_dict['count'] = 1

            if current_dict['count'] < idx + 1:
                break

    if len(root) == 0:
        return 0

    current_dict = root
    current_key = list(current_dict.keys())[0]
    while current_dict[current_key]['count'] == n_words:
        max_common += 1
        current_dict = current_dict[current_key]
        current_key = [key for key in current_dict.keys() if key != 'count'][0]

    return max_common


def run_tests():
    assert solution(["flower", "flow", "flight"]) == 2
    assert solution([]) == 0
    assert solution(["dog", "cat"]) == 0


if __name__ == '__main__':
    run_tests()
