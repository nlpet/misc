function solve()
    lines = readlines("input.txt")
    re_digits = r"(\d)"
    re_number_words = r"(one|two|three|four|five|six|seven|eight|nine)"

    word_to_digit = Dict(
        "one" => "1",
        "two" => "2",
        "three" => "3",
        "four" => "4",
        "five" => "5",
        "six" => "6",
        "seven" => "7",
        "eight" => "8",
        "nine" => "9"
    )

    calibration_value = 0

    for line in lines
        unit_range_digits = findall(re_digits, line)
        unit_range_words = findall(re_number_words, line; overlap=true)
        ranges = sort!(vcat(unit_range_digits, unit_range_words))
        a, z = line[ranges[1]], line[ranges[end]]

        a = get(word_to_digit, a, a)
        z = get(word_to_digit, z, z)
        n = parse(Int64, a * z)

        calibration_value += n
    end

    println("Calibration value: $calibration_value")
end

solve()