
function diffs(seq)
    diff = [y - x for (x, y) in zip(seq, seq[2:end])]
    return seq[end] + (any(x -> x != 0, diff) ? diffs(diff) : 0)
end

function parseline(line::String)::Vector{Int64}
    parse.(Int64, split(line, " "))
end

function solve()
    report = [parseline(line) for line in readlines("input.txt")]
    answer = sum([diffs(reverse(line)) for line in report])
    println("Answer: $answer")

end

solve()