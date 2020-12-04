import re


def is_valid_height(hgt):
    height = re.search(r"([0-9]+)(cm|in)", hgt)

    if not height:
        return False

    height, ms = height.groups()

    if ms == "cm" and 150 <= int(height) <= 193:
        return True
    elif ms == "in" and 59 <= int(height) <= 76:
        return True

    return False


def is_valid_hair_color(hcl):
    hair_color = re.search(r"#[a-f0-9]{6}", hcl)
    return hair_color is not None


def is_valid_passport_id(pid):
    passport_id = re.search(r"\d", pid)
    return passport_id is not None and len(pid) == 9


def is_passport_valid(fields, req_fields, n_req_fields):
    if not len(req_fields.intersection(fields.keys())) == n_req_fields:
        return False

    conditions = [
        len(fields["byr"]) == 4 and 1920 <= int(fields["byr"]) <= 2002,
        len(fields["iyr"]) == 4 and 2010 <= int(fields["iyr"]) <= 2020,
        len(fields["eyr"]) == 4 and 2020 <= int(fields["eyr"]) <= 2030,
        is_valid_height(fields["hgt"]),
        is_valid_hair_color(fields["hcl"]),
        fields["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        is_valid_passport_id(fields["pid"]),
    ]

    return all(conditions)


def main():
    valid_passports = 0
    req_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    n_req_fields = len(req_fields)
    patt = r"(\w{3}):([-@.\/#&+\w0-9]+)"

    with open("input.txt", "r") as fr:
        for passport in fr.read().split("\n\n"):
            passport_fields = dict(re.findall(patt, passport.strip()))

            if is_passport_valid(passport_fields, req_fields, n_req_fields):
                valid_passports += 1

    print(f"Number of valid passports: {valid_passports}")


if __name__ == "__main__":
    main()
