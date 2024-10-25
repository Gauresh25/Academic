data = {
    'T1': ['apple', 'banana', 'cherry', 'grape'],
    'T2': ['apple', 'banana', 'grape'],
    'T3': ['apple', 'cherry'],
    'T4': ['apple', 'banana', 'cherry'],
    'T5': ['banana', 'grape']
}

min_support = float(input("Enter the minimum support: "))
min_confidence = float(input('Enter the minimum confidence: '))

item_count = {}
for transaction in data.values():
    for item in transaction:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

total_transaction = len(data)
frequent_itemset = {}

for item, count in item_count.items():
    support = count / total_transaction
    if support >= min_support:
        frequent_itemset[item] = support

association_rule = []

for item in frequent_itemset.keys():
    for o_item in frequent_itemset.keys():
        if item != o_item:
            support_item = frequent_itemset[item]
            support_o_item = frequent_itemset[o_item]
            confidence = (support_item / support_o_item)
            if confidence >= min_confidence:
                association_rule.append((item, o_item, confidence))

print(association_rule)
for lhs, rhs, confidence in association_rule:
    print(f'{lhs} --> {rhs} : {round(confidence * 100)}')