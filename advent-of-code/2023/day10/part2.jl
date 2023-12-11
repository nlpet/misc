
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

function find_next_pipes(diagram, row, col, l, h)
    start = []
    row > 1 && diagram[row-1][col] in ['|', '7', 'F'] && push!(start, (row - 1, col))
    row < h && diagram[row+1][col] in ['|', 'L', 'J'] && push!(start, (row + 1, col))
    col > 1 && diagram[row][col-1] in ['-', 'L', 'F'] && push!(start, (row, col - 1))
    col < l && diagram[row][col+1] in ['-', 'J', '7'] && push!(start, (row, col + 1))
    start
end


function adjacent_tiles(row, col, l, h)
    adjacent = []
    row > 1 && push!(adjacent, (row - 1, col))
    row < h && push!(adjacent, (row + 1, col))
    col > 1 && push!(adjacent, (row, col - 1))
    col < l && push!(adjacent, (row, col + 1))
    adjacent
end

function find_s_orientation(start, next)
    row, col = start
    (row - 1, col) ∈ next && (row + 1, col) ∈ next && return 1
    (row - 1, col) ∈ next && (row, col + 1) ∈ next && return 1
    (row - 1, col) ∈ next && (row, col - 1) ∈ next && return 1
    return 0
end

function clean_map(diagram, loop, h, l)
    cleaned = []
    for i in 1:h
        line = [(i, j) ∉ loop ? '.' : diagram[i][j] for j in 1:l]
        push!(cleaned, join(line))
    end
    cleaned
end


function solve()
    diagram = readlines("input.txt")
    row, col = find_starting_position(diagram)
    h, l = length(diagram), length(diagram[1])
    (row1, col1), (row2, col2) = find_next_pipes(diagram, row, col, l, h)
    loop1 = [(row, col), (row1, col1)]
    loop2 = [(row, col), (row2, col2)]

    while true
        row1, col1 = move_to_connected_pipe(diagram, loop1)
        row2, col2 = move_to_connected_pipe(diagram, loop2)
        push!(loop1, (row1, col1))
        push!(loop2, (row2, col2))
        row1 == row2 && col1 == col2 && break
    end

    loop = Set(vcat(loop1, reverse(loop2[2:end-1])))
    visited = Set(loop)
    unvisited = Set([(i, j) for i in 1:h for j in 1:l])
    unvisited = setdiff(unvisited, visited)

    cleaned = clean_map(diagram, loop, h, l)
    orientation = find_s_orientation((row, col), ((row1, col1), (row2, col2)))
    vertical_pipes = orientation == 0 ? Set(['|', 'L', 'J']) : Set(['|', 'L', 'J', 'S'])
    in_loop = Set()

    for (row, col) in unvisited
        n = count(i -> (i ∈ vertical_pipes), cleaned[row][1:col])
        n % 2 == 1 && push!(in_loop, (row, col))
    end

    println("Answer: $(length(in_loop))")

end

solve()