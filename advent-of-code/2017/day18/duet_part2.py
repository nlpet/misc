# --- Day 18: Duet ---

from collections import defaultdict as dd
from typing import Any, Dict, List, Tuple
from queue import Queue


Program = Dict[str, Any]
Instructions = List[str]


def get(val: str, p: Program) -> int:
    try:
        return int(val)
    except ValueError:
        return p['regs'].get(val, 0)


def safe_get_lst(lst: List[Any], i: int) -> Any:
    try:
        return lst[i]
    except IndexError:
        return None


def run(i: int, ins: Instructions, pt: Program, po: Program) -> int:
    op, rv, val = ins[0], ins[1], safe_get_lst(ins, 2)

    if op == 'snd':
        po['msgs'].put(get(rv, pt))
        pt['sent'] += 1
    elif op == 'rcv':
        if pt['msgs'].empty():
            pt['locked'] = True
            return i
        else:
            pt['regs'][rv] = pt['msgs'].get()
            pt['locked'] = False
    elif op == 'jgz':
        v = get(rv, pt)
        if v > 0:
            return i + get(val, pt)
    else:
        val = get(val, pt)
        if op == 'set':
            pt['regs'][rv] = val
        elif op == 'add':
            pt['regs'][rv] += val
        elif op == 'mul':
            pt['regs'][rv] *= val
        elif op == 'mod':
            pt['regs'][rv] %= val

    return i + 1


def main():
    p0 = {'msgs': Queue(), 'regs': dd(int), 'sent': 0, 'locked': False}
    p1 = {'msgs': Queue(), 'regs': dd(int), 'sent': 0, 'locked': False}
    p1['regs']['p'] = 1

    with open('input.txt', 'r') as fr:
        ins = [line.strip().split(' ') for line in fr.readlines()]

    i, j = 0, 0

    while not p0['locked'] or not p0['locked']:
        i = run(i, ins[i], p0, p1)
        j = run(j, ins[j], p1, p0)

    print(p1['sent'])


if __name__ == '__main__':
    main()
