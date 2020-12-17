import re
import numpy as np

note_patt = re.compile(r"\w+: (\d+)-(\d+) or (\d+)-(\d+)")


def main():

    with open("input.txt", "r") as fr:
        sections = fr.read().strip().split("\n\n")

    notes = sections[0]
    nearby_tickets = sections[2].split("\n")[1:]

    plane = np.zeros(1000, dtype=int)

    for note in notes.split("\n"):
        match = re.search(note_patt, note)
        if match:
            rs = list(map(int, match.groups()))
            plane[rs[0] : rs[1] + 1] = 1
            plane[rs[2] : rs[3] + 1] = 1
        else:
            print("Invalid note format")

    error_rate = []

    for ticket in nearby_tickets:
        seats = [int(n) for n in ticket.split(",")]
        for seat in seats:
            if plane[seat] == 0:
                error_rate.append(seat)
                break

    print(sum(error_rate))


if __name__ == "__main__":
    main()
