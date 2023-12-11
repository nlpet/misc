using Combinatorics

function transpose_image(image::Vector{String})::Vector{String}
    transposed = []
    h, l = length(image), length(image[1])
    for col in 1:l
        line = [image[row][col] for row in 1:h]
        push!(transposed, join(line))
    end
    transposed
end


function expand(image::Vector{String})::Vector{String}
    expanded = []
    for row in image
        length(Set(row)) == 1 && push!(expanded, row)
        push!(expanded, row)
    end
    expanded
end

function distance(pair::Vector{Tuple{Int64,Int64}})
    (x1, y1), (x2, y2) = pair
    return abs(x2 - x1) + abs(y2 - y1)
end


function solve()
    image = readlines("test.txt")
    expanded = expand(image)
    expanded = transpose_image(expand(transpose_image(expanded)))
    h, l = length(expanded), length(expanded[1])
    galaxies = [(row, col) for row in 1:h for col in 1:l if expanded[row][col] == '#']
    pairs = collect(combinations(galaxies, 2))
    answer = sum([distance(pair) for pair in pairs])
    println("Answer: $answer")

end

solve()