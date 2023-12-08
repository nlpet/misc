
function process_network(desc::Vector{String})
    network = Dict()

    for node_info in desc
        node = node_info[1:3]
        l = node_info[8:10]
        r = node_info[13:15]
        network[node] = Dict('L' => l, 'R' => r)
    end
    network
end


function solve()
    lines = readlines("input.txt")
    instructions = lines[1]
    network_desc = lines[3:end]
    network = process_network(network_desc)

    num_instr = length(instructions)
    start = "AAA"
    finish = "ZZZ"
    steps = 0
    loc = 1

    while start != finish
        inst = instructions[loc]
        start = network[start][inst]
        steps += 1
        loc = loc == num_instr ? 1 : loc + 1
    end

    println("Answer: $steps")

end

solve()