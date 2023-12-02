
function is_game_possible(cubes::AbstractString, limits::Dict{String,Int64})::Bool
    for pick in split(cubes, ", ")
        n, colour = split(pick)
        limits[colour] < parse(Int64, n) && return false
    end
    true
end


function solve()
    lines = readlines("input.txt")
    limits = Dict("red" => 12, "green" => 13, "blue" => 14)
    answer = 0

    for line in lines
        game_tag, cubes = split(line, ": ")
        cubes = split(cubes, "; ")

        if all(map(g -> is_game_possible(g, limits), cubes))
            game_id = parse(Int64, split(game_tag)[2])
            answer += game_id
        end
    end

    println("Sum of possible game IDs: $answer")
end

solve()