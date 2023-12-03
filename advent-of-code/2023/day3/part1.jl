function get_adjacent(schematic::Vector{String}, row::Int64, range::UnitRange{Int64}, n::Int64)::String
    adj = Vector{String}()

    s, e = max(range.start - 1, 1), min(range.stop + 1, n)

    row > 1 && push!(adj, schematic[row-1][s:e]) # row above
    range.start > 1 && push!(adj, string(schematic[row][range.start-1])) # left square
    range.stop < n && push!(adj, string(schematic[row][range.stop+1])) # right square
    row < n && push!(adj, schematic[row+1][s:e]) # row below

    join(adj)
end


function contains_symbol(s::String)::Bool
    length(replace(s, r"[\.\d]+" => "")) > 0
end


function solve()
    schematic = readlines("input.txt")
    n = length(schematic)

    answer = 0
    for row in 1:n
        number_ranges = findall(r"(\d+)", schematic[row])
        for number_range in number_ranges
            adj = get_adjacent(schematic, row, number_range, n)
            if contains_symbol(adj)
                answer += parse(Int64, schematic[row][number_range])
            end
        end
    end

    println("Answer: $answer")
end

solve()