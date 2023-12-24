from sympy import solve_poly_system, symbols


def parse(line):
    pos, vel = line.strip().split(" @ ")
    pos = [int(n) for n in pos.split(", ")]
    vel = [int(n) for n in vel.split(", ")]
    return pos, vel


def solve():
    with open("input.txt") as fr:
        hailstones = [parse(line) for line in fr.readlines()]

    x, y, z, vx, vy, vz = symbols("x y z vx vy vz")

    equations = []
    ts = []

    for i, hailstone in enumerate(hailstones[:3]):
        (hs_x, hs_y, hs_z), (hs_vx, hs_vy, hs_vz) = hailstone
        t = symbols(f"t{i}")
        eq1 = x + vx * t - hs_x - hs_vx * t
        eq2 = y + vy * t - hs_y - hs_vy * t
        eq3 = z + vz * t - hs_z - hs_vz * t

        equations.extend([eq1, eq2, eq3])
        ts.append(t)

    (solution,) = solve_poly_system(equations, *([x, y, z, vx, vy, vz] + ts))
    px, py, pz, *_ = solution

    print(f"Answer: {px + py + pz}")


if __name__ == "__main__":
    solve()
