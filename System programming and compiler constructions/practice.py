ProdRules = {
    "E": [["T", "B"]],
    "B": [["+", "T", "B"], ["e"]],
    "T": [["F", "C"]],
    "C": [["+", "F", "C"], ["e"]],
    "F": [["(", "E", ")"], ["i"]]
}
startsymbol = 'E'
def findFirst(symbol):
    print("Recursive check for ",symbol)
    non_terminals = ProdRules.keys()
    firstset = []
    if symbol in non_terminals:
        for rules in ProdRules[symbol]:
            for rule in rules:

                if rule[0] == 'e' :
                    print("epsilon skipping")
                    if len(rule)>1:
                        firstset.extend(findFirst(rule[0]))
                    else:
                        continue
                if rule[0] not in non_terminals:
                    firstset.append(rule[0])
                if rule[0] in non_terminals:
                    firstset.extend(findFirst(rule[0]))


                break
    else:
        print("Symbol is a terminal")
        return

    return list(set(firstset))


def findFollow(symbol):
    followset =[]

    if symbol == startsymbol:
        followset.extend('$')
    for nt,productions in ProdRules.items():
        for prod in productions:
            if symbol in prod:
                for i in range(0,len(prod)):
                    if prod[i]==symbol and i<len(prod)-1:
                        followset.extend(prod[i+1])
                        break
                    if i == len(prod)-1:
                        print("hee")
                        followset.extend(findFirst(nt))
                print(prod)

    return followset

symbol ='B'
print("first is  ",findFirst(symbol))
print("follow is  ",findFollow(symbol))

nonTerminals = set(ProdRules.keys())
symbolset = set('$')
for nt,prod in ProdRules.items():
    for rule in prod:
        for symbol in rule:
            symbolset.add(symbol)
terminals = symbolset - nonTerminals

#print(nonTerminals,terminals)

parseTable={nont:{term: [] for term in terminals} for nont in nonTerminals}

for nonTerminal,productions in ProdRules.items():
    firstset = findFirst(nonTerminal)

    for item in firstset:
        if item !='e':
            parseTable[nonTerminal][item]= productions
        else:
            for i in findFollow(nonTerminal):
                parseTable[nonTerminal][i] = productions


for i,v in parseTable.items():
    print(i,v,sep="   |   ")