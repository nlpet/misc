def find_pairs_of_brackets(s):
    brackets = []
    stack = []

    for idx, ch in enumerate(s):
        if ch == "(":
            stack.append(idx)
        elif ch == ")":
            brackets.append((stack.pop(), idx))

    return brackets


def evaluate_expression(expr):
    op = "+"
    result = 0

    for item in expr:
        if item.isdigit():
            if op == "+":
                result += int(item)
            elif op == "*":
                result *= int(item)
        elif item in {"*", "+"}:
            op = item

    return result


def evaluate_expressions(s, brackets):
    expr = list(s)

    for i, j in brackets:
        result = evaluate_expression(expr[i : j + 1])
        expr = expr[:i] + [str(result)] + [" "] * (j - i) + expr[j + 1 :]

    return evaluate_expression(expr)


def main():
    total = 0
    with open("input.txt", "r") as fr:
        for line in fr.readlines():
            expr = line.strip().replace(" ", "")
            brackets = find_pairs_of_brackets(expr)
            result = evaluate_expressions(expr, brackets)
            total += result

    print(total)


if __name__ == "__main__":
    main()
