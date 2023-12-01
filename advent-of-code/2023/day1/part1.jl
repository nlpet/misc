function solve()
    lines = readlines("input.txt")
    cvs = [l[r[1]] * l[r[end]] for (l, r) in zip(lines, findall.(r"(\d)", lines))]
    cv = sum(parse.(Int64, cvs))
    println("Calibration value: $(cv)")
end

solve()