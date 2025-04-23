from collections import defaultdict
from tabulate import tabulate

ProdRules = {
    "E": [["T", "A"]],
    "A": [["+", "T", "A"], ["e"]],
    "T": [["F", "B"]],
    "B": [["+", "F", "B"], ["e"]],
    "F": [["(", "E", ")"], ["id"]]
}

def findFirst(ProdRules, symbol):
    nonTerminal = list(ProdRules.keys())
    firstset = []

    if symbol not in ProdRules:
        return [symbol]  # It's a terminal, so return itself in the FIRST set

    if symbol in ProdRules:
        productions = ProdRules[symbol]
        for rule in productions:
            i = 0
            while i < len(rule):
                if rule[i] == "e":  # Skip epsilon and continue checking next symbols
                    i += 1
                    continue

                if rule[i] in nonTerminal:  # If it's a non-terminal, recurse to get its FIRST set
                    firstset.extend(findFirst(ProdRules, rule[i]))
                    break  # We stop after adding the FIRST of the first non-terminal we encounter
                else:  # If it's a terminal, add it to the FIRST set
                    firstset.append(rule[i])
                    break  # Stop after encountering the first terminal symbol
            else:  # This else is for the case where we have epsilon productions
                firstset.append("e")

    return firstset

def findFollow(ProdRules, symbol, start_symbol):
    followset = set()

    if symbol == start_symbol:
        followset.add('$')  # Add end of input symbol to the start symbol's follow set

    for nonterminal, productions in ProdRules.items():
        for production in productions:
            try:
                symbol_pos = production.index(symbol)

                if symbol_pos < len(production) - 1:
                    next_symbol = production[symbol_pos + 1]

                    if next_symbol not in ProdRules:
                        followset.add(next_symbol)
                    else:
                        first_of_next = set(findFirst(ProdRules, next_symbol))
                        if 'e' in first_of_next:  # If epsilon is in FIRST set
                            first_of_next.remove('e')
                            followset.update(first_of_next)
                            followset.update(findFollow(ProdRules, nonterminal, start_symbol))
                        else:
                            followset.update(first_of_next)

                elif symbol_pos == len(production) - 1 and nonterminal != symbol:
                    followset.update(findFollow(ProdRules, nonterminal, start_symbol))

            except ValueError:
                continue

    return list(followset)


def createTable(ProdRules, first_set, follow_set):
    terminals = set()
    non_terminals = set(ProdRules.keys())

    # Collect all terminals from the productions
    for non_terminal in ProdRules:
        for production in ProdRules[non_terminal]:
            for symbol in production:
                if symbol not in ProdRules and symbol != 'e':
                    terminals.add(symbol)
    terminals.add('$')  # Add $ for the end of input

    # Initialize the parse table (a dictionary of dictionaries)
    parse_table = {non_terminal: {terminal: [] for terminal in terminals} for non_terminal in non_terminals}

    # Fill in the parse table
    for non_terminal in ProdRules:
        for production in ProdRules[non_terminal]:
            first_of_production = findFirst(ProdRules, production[0])
            print(first_of_production)

            for terminal in first_of_production:
                if terminal != 'e':  # Don't add epsilon to the table
                    parse_table[non_terminal][terminal] = production
                else:  # If epsilon is in the FIRST set, we must consider FOLLOW
                    for follow_symbol in follow_set[non_terminal]:
                        parse_table[non_terminal][follow_symbol] = production

    return parse_table


# Compute FIRST and FOLLOW sets
first_set = defaultdict(list)
follow_set = defaultdict(list)

for key in ProdRules:
    first_set[key] = findFirst(ProdRules, key)
    follow_set[key] = findFollow(ProdRules, key, "E")

# Generate the LL(1) parse table
parse_table = createTable(ProdRules, first_set, follow_set)

# Printing the LL(1) Parsing Table in a table format using tabulate
# We prepare the data for tabulate
headers = ['Non-Terminals'] + list({terminal for terminals in parse_table.values() for terminal in terminals.keys()})

table_data = []

for non_terminal, row in parse_table.items():
    row_data = [non_terminal]
    for terminal in headers[1:]:
        if terminal in row:
            row_data.append(" ".join(row[terminal]))
        else:
            row_data.append("")
    table_data.append(row_data)

# Display the table
print(tabulate(table_data, headers=headers, tablefmt="grid"))