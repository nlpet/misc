def main():
    with open("input.txt", "r") as fr:
        seen, target = set([]), 2020
        for line in fr.readlines():
            num = int(line.strip())
            if target - num in seen:
                print(f"{num}x{target - num}={num * (target - num)}")
                break
            else:
                seen.add(num)


if __name__ == "__main__":
    main()
