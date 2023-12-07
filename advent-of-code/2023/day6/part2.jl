
function solve()
    times, distances = readlines("input.txt")
    time = parse(Int64, reduce(*, split(strip(split(times, ":")[2]))))
    dist = parse(Int64, reduce(*, split(strip(split(distances, ":")[2]))))
    n = 0

    for vel in 0:time
        n += time * vel > dist ? 1 : 0
        time -= 1
    end

    println("Answer : $n")

end

solve()