from collections import Counter


def main():
    with open("input.txt", "r") as fr:
        total = 0

        for group in fr.read().split("\n\n"):
            group_size = len(group.strip().split("\n"))
            answers = Counter(group.replace("\n", ""))
            group_total = 0

            for group_count in answers.values():
                if group_count == group_size:
                    group_total += 1

            total += group_total

        print(f"The sum of the counts is {total}")


if __name__ == "__main__":
    main()
