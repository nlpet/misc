using Combinatorics

function distance(pair::Vector{Tuple{Int64,Int64}})
    (x1, y1), (x2, y2) = pair
    return abs(x2 - x1) + abs(y2 - y1)
end

function solve()
    image = readlines("input.txt")
    h, l = length(image), length(image[1])
    galaxies = [(row, col) for row in 1:h for col in 1:l if image[row][col] == '#']
    pairs = collect(combinations(galaxies, 2))
    empty_rows = [i for i in 1:h if length(Set(image[i])) == 1]
    empty_cols = [j for j in 1:l if length(Set([image[i][j] for i in 1:h])) == 1]
    magnitude = 1000000
    answer = 0

    for pair in pairs
        (r1, c1), (r2, c2) = pair
        dist = distance(pair)
        dist += sum([min(r1, r2) <= i <= max(r1, r2) ? magnitude - 1 : 0 for i in empty_rows])
        dist += sum([min(c1, c2) <= j <= max(c1, c2) ? magnitude - 1 : 0 for j in empty_cols])
        answer += dist
    end

    println("Answer: $answer")
end

solve()