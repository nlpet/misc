
function find_starting_position(diagram)
    for row in eachindex(diagram)
        rng = findfirst("S", diagram[row])
        !isnothing(rng) && return (row, rng.start)
    end
end

function move_to_connected_pipe(diagram, loop)
    prev = loop[end-1]
    row, col = loop[end]
    pipe = diagram[row][col]

    pipe == '|' && prev == (row - 1, col) && return (row + 1, col)
    pipe == '|' && prev == (row + 1, col) && return (row - 1, col)

    pipe == '-' && prev == (row, col - 1) && return (row, col + 1)
    pipe == '-' && prev == (row, col + 1) && return (row, col - 1)

    pipe == 'L' && prev == (row, col + 1) && return (row - 1, col)
    pipe == 'L' && prev == (row - 1, col) && return (row, col + 1)

    pipe == 'J' && prev == (row - 1, col) && return (row, col - 1)
    pipe == 'J' && prev == (row, col - 1) && return (row - 1, col)

    pipe == '7' && prev == (row, col - 1) && return (row + 1, col)
    pipe == '7' && prev == (row + 1, col) && return (row, col - 1)

    pipe == 'F' && prev == (row + 1, col) && return (row, col + 1)
    pipe == 'F' && prev == (row, col + 1) && return (row + 1, col)
end

function find_next_pipes(diagram, row, col)
    l = length(diagram)
    start = []
    row > 1 && diagram[row-1][col] in ['|', '7', 'F'] && push!(start, (row - 1, col))
    row < l && diagram[row+1][col] in ['|', 'L', 'J'] && push!(start, (row + 1, col))
    col > 1 && diagram[row][col-1] in ['-', 'L', 'F'] && push!(start, (row, col - 1))
    col < l && diagram[row][col+1] in ['-', 'J', '7'] && push!(start, (row, col + 1))
    start
end


function solve()
    diagram = readlines("input.txt")
    row, col = find_starting_position(diagram)
    (row1, col1), (row2, col2) = find_next_pipes(diagram, row, col)
    loop1 = [(row, col), (row1, col1)]
    loop2 = [(row, col), (row2, col2)]

    while true
        row1, col1 = move_to_connected_pipe(diagram, loop1)
        row2, col2 = move_to_connected_pipe(diagram, loop2)
        push!(loop1, (row1, col1))
        push!(loop2, (row2, col2))
        row1 == row2 && col1 == col2 && break
    end

    println("Answer: $(length(loop1) - 1)")

end

solve()