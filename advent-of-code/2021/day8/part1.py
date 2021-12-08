# --- Day 8: Seven Segment Search ---


def solution():
    unique_number_of_segments = 0

    with open("input.txt") as fr:
        for line in fr.readlines():
            _, output_value = line.strip().split(" | ")
            sx = output_value.split(" ")
            unique_number_of_segments += sum(
                [1 if len(s) in {2, 3, 4, 7} else 0 for s in sx]
            )

    print(unique_number_of_segments)


if __name__ == "__main__":
    solution()
