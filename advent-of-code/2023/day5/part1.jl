function find_id_mapping(category_mapping::Dict{UnitRange{Int64},Int64}, id::Int64)::Int64
    for (range, offset) in category_mapping
        id in range && return id + offset
    end
    id
end

function category_mapping(mapping::AbstractString)
    category_mapping = Dict{UnitRange{Int64},Int64}()

    for range in split(strip(split(mapping, ":")[2]), "\n")
        dest, source, l = parse.(Int64, split(range))
        category_mapping[source:source+l-1] = dest - source
    end
    category_mapping
end

function solve()
    almanac = split(read("input.txt", String), "\n\n")
    seeds, mappings = almanac[1], almanac[2:end]
    ids = parse.(Int64, split(split(seeds, ": ")[2]))

    for mapping in mappings
        cm = category_mapping(mapping)
        ids = [find_id_mapping(cm, id) for id in ids]
    end

    println("Lowest location number: $(minimum(ids))")
end

solve()