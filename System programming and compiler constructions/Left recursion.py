from collections import defaultdict

Prod_rules = {
    'A': [['A', 'B', 'd'], ['A', 'a'], ['c']],
    'B': [['B', 'e'], ['b']]
}


def remove_left_recursion(rules):
    new_rules = defaultdict(list)

    for non_terminal in rules:
        left_rec = []
        non_left_rec = []
        new_non_terminal = non_terminal + "1"

        for production in rules[non_terminal]:
            if production[0] == non_terminal:
                # Left-recursive production
                left_rec.append(production[1:] + [new_non_terminal])
            else:
                # Non-left-recursive production
                non_left_rec.append(production + [new_non_terminal])
        if left_rec:
            # Update the rules
            new_rules[non_terminal].extend(non_left_rec)
            new_rules[new_non_terminal] = [p for p in left_rec] + [["ε"]]
        else:
            new_rules[non_terminal].extend(rules[non_terminal])

    return dict(new_rules)


new_grammar = remove_left_recursion(Prod_rules)
for nt, prods in new_grammar.items():
    print(f"{nt} -> {[' '.join(p) for p in prods]}")