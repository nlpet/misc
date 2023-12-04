
function process_cards(cards::Vector{String})::Dict{Int64,Int64}
    cards_info = Dict()

    for card in cards
        card_tag, numbers = split(card, ": ")
        card_number = parse(Int64, split(card_tag)[2])
        card_numbers, winning_numbers = map(split, split(numbers, " | "))
        card_winning_numbers = length(intersect(card_numbers, winning_numbers))
        cards_info[card_number] = card_winning_numbers
    end
    cards_info
end

function solve()
    cards = readlines("input.txt")
    cards_info = process_cards(cards)

    n_cards = 0
    queue = collect(keys(cards_info))

    while length(queue) > 0
        n_cards += 1
        next_card = popfirst!(queue)
        matches = cards_info[next_card]

        length(matches) == 0 && continue

        for card in next_card+1:next_card+matches
            push!(queue, card)
        end
    end
    println("Total scratchpads: $n_cards")
end

solve()