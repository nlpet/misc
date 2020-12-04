import re


def main():
    valid_passports = 0
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    num_required_fields = len(required_fields)
    patt = r"(\w{3}):([-@.\/#&+\w0-9]+)"

    with open("input.txt", "r") as fr:
        for passport in fr.read().split("\n\n"):
            parsed_passport = re.findall(patt, passport.strip())
            fields = [k for k, v in parsed_passport]

            if len(required_fields.intersection(fields)) == num_required_fields:
                valid_passports += 1

    print(f"Number of valid passports: {valid_passports}")


if __name__ == "__main__":
    main()
