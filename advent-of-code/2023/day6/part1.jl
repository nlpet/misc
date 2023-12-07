
function solve()
    times, distances = readlines("input.txt")
    times = parse.(Int64, split(strip(split(times, ":")[2])))
    distances = parse.(Int64, split(strip(split(distances, ":")[2])))

    answer = 1

    for (t, d) in zip(times, distances)
        n = 0
        for vel in 0:t
            n += t * vel > d ? 1 : 0
            t -= 1
        end
        answer *= n
    end
    println("Answer : $answer")
end

solve()