
function solve()
    cards = readlines("input.txt")
    answer = 0

    for card in cards
        numbers = split(card, ": ")[2]
        card_numbers, winning_numbers = map(split, split(numbers, " | "))
        card_winning_numbers = length(intersect(card_numbers, winning_numbers))
        answer += card_winning_numbers > 0 ? 2^(card_winning_numbers - 1) : 0
    end
    println("Answer: $answer")
end

solve()