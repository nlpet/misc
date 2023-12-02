
function parse_game_cubes(line::String)::Vector{SubString{String}}
    _, games = split(line, ": ")
    reduce(vcat, split.(split(games, "; "), ", "))
end

function solve()
    lines = readlines("input.txt")
    answer = 0

    for line in lines
        min_cubes = Dict("blue" => 0, "red" => 0, "green" => 0)
        cubes = parse_game_cubes(line)

        for cube in cubes
            n, colour = split(cube)
            n = parse(Int64, n)
            if min_cubes[colour] < n
                min_cubes[colour] = n
            end
        end

        answer += reduce(*, values(min_cubes))
    end

    println("Answer: $answer")
end

solve()