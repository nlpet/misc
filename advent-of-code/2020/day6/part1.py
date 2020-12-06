def main():
    with open("input.txt", "r") as fr:
        counts = [
            len(set(group.replace("\n", ""))) for group in fr.read().split("\n\n")
        ]

        print(f"The sum of the counts is {sum(counts)}")


if __name__ == "__main__":
    main()
