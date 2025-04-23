ProdRules = dict()

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
    # print(nonTerminal)
    if symbol not in ProdRules.keys():
        print("Start symbol is terminal")

    if symbol in ProdRules.keys():
        productions = ProdRules[symbol]
        # print(productions)
        for rule in productions:
            i = 0
            if rule[i] == "e":
                i += 1
                continue
            if rule[i] in nonTerminal:
                firstset.extend(findFirst(ProdRules, rule[i]))
                break
            else:
                firstset.append(rule[0])

    return firstset

def findFollow(ProdRules, symbol, start_symbol):
    followset = []

    if symbol == start_symbol:
        followset.append('$')

    for nonterminal, productions in ProdRules.items():
        for production in productions:
            if symbol in production:
                for i in range(0,len(production)):
                    if production[i]==symbol:
                        print(production)
                        break

                if i == len(production)-1 and symbol != nonterminal:#last element
                    followset.append(findFollow(ProdRules,nonterminal,start_symbol))
                else:
                    followset.append(findFirst(ProdRules,production[i+1]))
            else:
                pass

    return list(followset)

start_symbol = 'E'

print("First set is : ",findFirst(ProdRules,start_symbol))

print("Follow set for E:", findFollow(ProdRules, "E", start_symbol))
# print("Follow set for T:", findFollow(ProdRules, "T", start_symbol))
# print("Follow set for F:", findFollow(ProdRules, "F", start_symbol))