# --- Day 9: Explosives in Cyberspace ---

from collections import namedtuple
from copy import deepcopy
from typing import List, Any
import re


Sections = List[List[int]]

CHARS_REG = re.compile(r'\b[A-Z]+\b')
BRACKETS_REG = re.compile(r'\((\d+)x(\d+)\)')


def add_chars_section(sections: Sections, match: Any, index: int) -> int:
    length = len(match.group())
    sections.append([0, length, length])
    return index + length


def add_brackets_section(sections: Sections, match: Any, index: int) -> int:
    subsequent, repeat = map(int, match.groups())
    length = match.span()[1] - match.span()[0]
    sections.append([subsequent, repeat, repeat, length])
    return index + length


def add_section(s: str, index: int, sections: Sections) -> int:
    match_brackets = BRACKETS_REG.search(s[index:])
    match_chars = CHARS_REG.search(s[index:])

    if match_brackets and match_chars:
        if match_chars.span()[0] < match_brackets.span()[0]:
            index = add_chars_section(sections, match_chars, index)
        else:
            index = add_brackets_section(sections, match_brackets, index)
    elif match_brackets:
        index = add_brackets_section(sections, match_brackets, index)
    elif match_chars:
        index = add_chars_section(sections, match_chars, index)

    return index


def process_sections(sections: Sections) -> Sections:
    i = 0
    sections = deepcopy(sections)

    while i < len(sections):
        if sections[i][0] == 0:
            if i > 0 and sections[i - 1][0] != 0:
                subsequent, orig_repeat, repeat, length = sections[i - 1]
                new_len = subsequent * repeat + sections[i][1] - subsequent
                sections[i][2] = new_len
            i += 1
        else:
            subsequent, orig_repeat, repeat, length = sections[i]
            j = i + 1
            while subsequent > 0:
                if sections[j][0] == 0:
                    _, orig_len, len_ = sections[j]
                    if subsequent > len_:
                        subsequent -= len_
                        sections[j][2] = len_ * repeat
                    else:
                        new_len = subsequent * repeat + orig_len - subsequent
                        sections[j][2] = new_len
                        subsequent = 0
                else:
                    sections[j][2] *= orig_repeat
                    subsequent -= sections[j][3]
                j += 1
            i += 1
    return sections


def get_decompressed_size(sections: Sections) -> int:
    return sum([item[2] for item
                in filter(lambda item: item[0] == 0, sections)])


def main() -> None:
    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            sections: Sections = []
            index = 0
            s = line.strip()
            while index < len(s):
                index = add_section(s, index, sections)
            processed_sections = process_sections(sections)
            print(get_decompressed_size(processed_sections))


if __name__ == '__main__':
    main()
