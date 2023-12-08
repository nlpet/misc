
function process_network(desc::Vector{String})::Dict{String,Dict{Char,String}}
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
    start = collect(filter(k -> endswith(k, "A"), keys(network)))
    results = Dict()

    for s in start
        node, step, loc = s, 1, true
        while isnothing(get(results, s, nothing))
            inst = instructions[loc]
            node = network[node][inst]
            loc = loc == num_instr ? 1 : loc + 1
            if endswith(node, "Z")
                results[s] = step
            end
            step += 1
        end
    end

    steps = values(results)
    answer = lcm(steps...)
    println("Answer: $answer")

end

solve()