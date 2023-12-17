import heapq


def solve():
    with open("input.txt") as fr:
        mapp = [[int(n) for n in l.strip()] for l in fr.readlines()]

    h, l = len(mapp), len(mapp[0])

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = [(0, 0, 0, 0, 0, 0)]
    seen = set()

    while queue:
        dist, row, col, dr, dc, steps = heapq.heappop(queue)

        if row == h - 1 and col == l - 1:
            print(dist)
            break

        if (row, col, dr, dc, steps) in seen:
            continue

        seen.add((row, col, dr, dc, steps))

        if steps < 3 and (dr, dc) != (0, 0):
            next_row, next_col = row + dr, col + dc
            if 0 <= next_row < h and 0 <= next_col < l:
                cost = dist + mapp[next_row][next_col]
                state = (cost, next_row, next_col, dr, dc, steps + 1)
                heapq.heappush(queue, state)

        for next_dr, next_dc in directions:
            if (next_dr, next_dc) != (dr, dc) and (next_dr, next_dc) != (-dr, -dc):
                next_row, next_col = row + next_dr, col + next_dc
                if 0 <= next_row < h and 0 <= next_col < l:
                    cost = dist + mapp[next_row][next_col]
                    state = (cost, next_row, next_col, next_dr, next_dc, 1)
                    heapq.heappush(queue, state)


if __name__ == "__main__":
    solve()
