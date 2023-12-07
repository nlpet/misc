import StatsBase: countmap


function hand_type(hand::AbstractString)
    hand_repr = collect(values(countmap(hand)))
    sort!(hand_repr, rev=true)

    hand_repr[1] == 5 && return 1
    hand_repr[1] == 4 && return 2
    hand_repr[1] == 3 && hand_repr[2] == 2 && return 3
    hand_repr[1] == 3 && return 4
    hand_repr[1] == 2 && hand_repr[2] == 2 && return 5
    hand_repr[1] == 2 && return 6
    return 7
end

function card_value(card::Char)
    if card in '2':'9'
        return parse(Int, string(card))
    elseif card == 'T'
        return 10
    elseif card == 'J'
        return 11
    elseif card == 'Q'
        return 12
    elseif card == 'K'
        return 13
    elseif card == 'A'
        return 14
    end
end

function hand_values(hand::AbstractString)
    return [card_value(c) for c in hand]
end

function compare_hands(hand1::AbstractString, hand2::AbstractString)
    ht1 = hand_type(hand1)
    ht2 = hand_type(hand2)

    ht1 !== ht2 && return ht1 < ht2

    values1 = hand_values(hand1)
    values2 = hand_values(hand2)

    for i in 1:min(length(values1), length(values2))
        if values1[i] != values2[i]
            return values1[i] > values2[i]
        end
    end
    return length(values1) > length(values2)
end

function sort_hands(hands::Vector{SubString{String}})
    sort(hands, lt=(x, y) -> compare_hands(x, y), rev=true)
end


function solve()
    lines = [split(line) for line in readlines("input.txt")]
    mapping = Dict([line[1] => parse(Int64, line[2]) for line in lines])
    hands = collect(keys(mapping))
    hands = sort_hands(hands)

    answer = 0

    for (i, hand) in enumerate(hands)

        answer += i * mapping[hand]
    end

    println("Answer: $answer")
end

solve()