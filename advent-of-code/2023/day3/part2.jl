
function adjacent_row_numbers!(numbers::Vector{Int64}, s::String, i::Int64)
    number_ranges = findall(r"(\d+)", s)
    for nr in number_ranges
        if length(intersect(nr, i-1:i+1)) > 0
            push!(numbers, parse(Int64, s[nr]))
        end
    end
end

function adjacent_numbers(schematic::Vector{String}, row::Int64, i::Int64, n::Int64)::Vector{Int64}
    numbers = Vector{Int64}()

    row > 1 && adjacent_row_numbers!(numbers, schematic[row-1], i) # row above
    row < n && adjacent_row_numbers!(numbers, schematic[row+1], i) # row below

    # on the left or on the right
    number_ranges = findall(r"(\d+)", schematic[row])
    for nr in number_ranges
        if nr.stop == i - 1 || nr.start == i + 1
            push!(numbers, parse(Int64, schematic[row][nr]))
        end
    end
    numbers
end

function solve()
    schematic = readlines("input.txt")
    n = length(schematic)

    answer = 0
    for row in 1:n
        gear_ranges = findall("*", schematic[row])
        for gear_range in gear_ranges
            nums = adjacent_numbers(schematic, row, gear_range.start, n)
            answer += length(nums) == 2 ? prod(nums) : 0
        end
    end

    println("Answer: $answer")
end

solve()