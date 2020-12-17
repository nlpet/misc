import re
import numpy as np
from functools import partial

note_patt = re.compile(r"([a-z\s]+): (\d+)-(\d+) or (\d+)-(\d+)")


def create_rule(a, b, c, d, lst):
    return sum(lst[0:a]) + sum(lst[b + 1 : c]) + sum(lst[d + 1 :]) == 0


def create_rule_single_seat(a, b, c, d):
    return lambda n: a <= n <= b or c <= n <= d


def is_ticket_valid(seats, rules):
    valid_seats = 0
    for seat in seats:
        for rfn in rules.values():
            if rfn(seat):
                valid_seats += 1
                break

    return valid_seats == len(seats)


def parse_notes(notes):
    rules = {}
    rules_single_seats = {}

    for note in notes.split("\n"):
        match = re.search(note_patt, note)
        if match:
            parts = match.groups()
            field_name = parts[0]
            rs = list(map(int, parts[1:]))
            rules[field_name] = partial(create_rule, *rs)
            rules_single_seats[field_name] = create_rule_single_seat(*rs)
        else:
            print("Invalid note format")

    return rules, rules_single_seats


def get_valid_tickets(nearby_tickets, rules_single_seats):
    valid_nearby_tickets = []

    for ticket in nearby_tickets:
        seats = [int(n) for n in ticket.split(",")]
        if is_ticket_valid(seats, rules_single_seats):
            valid_nearby_tickets.append(seats)

    return valid_nearby_tickets


def get_candidates(valid_nearby_tickets, rules):
    candidates = {k: [] for k in rules}
    filled_seats = [
        np.zeros(1000, dtype=int).tolist() for _ in range(len(rules.keys()))
    ]

    for seats in valid_nearby_tickets:
        for idx, seat in enumerate(seats):
            filled_seats[idx][seat] = 1

    for idx, fs in enumerate(filled_seats):
        for field_name, rfn in rules.items():
            if rfn(fs):
                candidates[field_name].append(idx)

    return candidates


def find_mapping(candidates, rules):
    matched = set([])
    mapping = {}

    for i in range(1, len(rules.keys()) + 1):
        for field_name, idxs in candidates.items():
            if len(idxs) == i:
                for idx in idxs:
                    if idx not in matched:
                        matched.add(idx)
                        mapping[field_name] = idx

    return mapping


def main():

    with open("input.txt", "r") as fr:
        sections = fr.read().strip().split("\n\n")

    notes = sections[0]
    my_ticket = [int(n) for n in sections[1].split("\n")[1].split(",")]
    nearby_tickets = sections[2].split("\n")[1:]

    rules, rules_single_seats = parse_notes(notes)
    valid_nearby_tickets = get_valid_tickets(nearby_tickets, rules_single_seats)
    candidates = get_candidates(valid_nearby_tickets, rules)
    mapping = find_mapping(candidates, rules)

    result = 1

    for field_name, idx in mapping.items():
        if field_name.startswith("departure"):
            result *= my_ticket[idx]

    print(result)


if __name__ == "__main__":
    main()
