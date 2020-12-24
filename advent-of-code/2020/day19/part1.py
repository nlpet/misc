import regex


def construct_regex_patt(rules):
    def wrap(rule_id):
        if rule_id.isdigit():
            wrapped = map(wrap, rules[rule_id].split())
            return "({})".format("".join(wrapped))
        return rule_id

    return regex.compile(wrap("0"))


def main():
    rules = {}

    with open("input.txt", "r") as fr:
        unparsed_rules, messages = fr.read().split("\n\n")
        messages = messages.strip().split("\n")

        for rule in unparsed_rules.split("\n"):
            rule_id, rule = rule.strip().split(": ")
            rule = rule.strip('"')
            rules[rule_id] = rule

    patt = construct_regex_patt(rules)
    result = sum(patt.fullmatch(m) is not None for m in messages)
    print(result)
    # rules["8"] = "42 +"  # repeat pattern
    # rules["11"] = "(?P<R> 42 (?&R)? 31 )"  # recursive pattern
    # print(match_messages(rules, messages))


if __name__ == "__main__":
    main()
