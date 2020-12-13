def main():
    with open("input.txt", "r") as fr:
        contents = fr.readlines()
        ts = int(contents[0].strip())
        buses = contents[1].strip().split(",")

    shortest_delay = ts
    result = 0

    for bus in buses:
        if bus == "x":
            continue

        bus_id = int(bus)
        delay = bus_id - (ts % bus_id)

        if delay < shortest_delay:
            shortest_delay = delay
            result = delay * bus_id

    print(result)


if __name__ == "__main__":
    main()
