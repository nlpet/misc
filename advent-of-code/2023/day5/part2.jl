function category_mapping(mapping::AbstractString)::Vector{Vector{Int64}}
    [parse.(Int64, split(range)) for range in split(strip(split(mapping, ":")[2]), "\n")]
end


function find_mapping(cm, ranges)
    overlaps = []

    for (dest, src, l) in cm
        src_stop = src + l
        newranges = []

        while length(ranges) > 0
            start, stop = pop!(ranges)
            before = (start, min(stop, src))
            o = (max(start, src), min(src_stop, stop))
            after = (max(src_stop, start), stop)

            before[2] > before[1] && push!(newranges, before)
            o[2] > o[1] && push!(overlaps, (o[1] - src + dest, o[2] - src + dest))
            after[2] > after[1] && push!(newranges, after)
        end
        ranges = newranges
    end
    return vcat(overlaps, ranges)
end


function solve()
    almanac = split(read("input.txt", String), "\n\n")
    seeds, mappings = almanac[1], almanac[2:end]
    seeds = parse.(Int64, split(split(seeds, ": ")[2]))
    pairs = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in 1:2:length(seeds)-1]
    cms = [category_mapping(m) for m in mappings]
    answer = []

    for pair in pairs
        ranges = [pair]
        for cm in cms
            ranges = find_mapping(cm, ranges)
        end
        push!(answer, minimum(ranges)[1])
    end
    println("Answer: $(minimum(answer))")
end

solve()