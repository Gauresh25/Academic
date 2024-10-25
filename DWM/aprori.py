from collections import defaultdict
from itertools import combinations

transactions = [{1, 2}, {1, 2, 3}, {1}, {1, 2, 3},{1, 2, 3},{1,2,5},{1,4,5}]
min_support = 0.3
min_confidence = 0.7


# Finding L0 (single items)
def find_single_item_frequencies_v2(transactions):
    counts = defaultdict(int)
    total_transactions = len(transactions)

    for transaction in transactions:
        for item in transaction:
            counts[item] += 1

    print("L0 frequency:")
    support = dict(filter(lambda x: x[1] / total_transactions >= min_support, counts.items()))
    result =  {frozenset([item]): obj / total_transactions for item, obj in support.items()}
    print(result)
    return result


# Self join for getting candidates
def self_join(prev_supp_set, k):
    candidates = []
    prev_set = list(prev_supp_set.keys())

    for i in range(len(prev_set)):
        for j in range(i + 1, len(prev_set)):
            s1 = set(prev_set[i])
            s2 = set(prev_set[j])

            if len(s1.union(s2)) == k:
                candidates.append(s1.union(s2))

    return candidates


# Calculate support for candidate sets
def get_support(transactions, itemset):
    count = 0
    total_transactions = len(transactions)

    # Go through each transaction
    for transaction in transactions:
        # Check if itemset is subset of transaction
        if itemset.issubset(transaction):
            count += 1

    support = count / total_transactions
    return support

# Find frequent itemsets for level k
def find_frequent_k_sets(transactions, candidates, min_support):
    return dict(
        filter(
            lambda x: x[1] >= min_support,
            {
                frozenset(candidate): get_support(transactions, candidate)
                for candidate in candidates
            }.items()
        )
    )
"""
def find_frequent_k_sets(transactions, candidates, min_support):
    # Step 1: Create dictionary of candidate:support pairs
    candidate_supports = {}
    for candidate in candidates:
        support = get_support(transactions, candidate)
        candidate_supports[frozenset(candidate)] = support
    
    # Step 2: Filter based on min_support
    frequent_sets = {}
    for candidate, support in candidate_supports.items():
        if support >= min_support:
            frequent_sets[candidate] = support
            
    # Step 3: Return filtered dictionary
    return frequent_sets
"""


# Main Apriori algorithm
def apriori(transactions, min_support):
    # Get L1 (frequent single items)
    result = []
    L1 = find_single_item_frequencies_v2(transactions)
    print("L1:", L1)
    result.append(L1)

    k = 2
    while True:
        # Get previous level's frequent sets
        prev_frequent_sets = result[-1]
        if not prev_frequent_sets:
            break

        # Generate candidates through self_join
        candidates = self_join(prev_frequent_sets, k)
        if not candidates:
            break

        # Find frequent k-itemsets
        print("for k>1 itemsets:")
        frequent_k = find_frequent_k_sets(transactions, candidates, min_support)
        print(f"L{k}:", frequent_k)

        if frequent_k:
            result.append(frequent_k)
        else:
            break
        k += 1

    return result


# Generate association rules
def generate_rules(freq_itemsets, min_confidence):
    """
    freq_itemsets looks like:
    [
        {frozenset({1}): 1.0, frozenset({2}): 0.75},           # L1
        {frozenset({1, 2}): 0.75},                             # L2
        {frozenset({1, 2, 3}): 0.5}                            # L3
    ]
    """
    rules = []

    # Skip L1 (single items) as they can't make rules
    for k_itemsets in freq_itemsets[1:]:  # Start from L2
        # k_itemsets is like {frozenset({1, 2}): 0.75}

        for itemset, support in k_itemsets.items():
            # itemset might be {1, 2}, support is 0.75

            # For each length from 1 to len(itemset)-1
            for i in range(1, len(itemset)):
                # If itemset is {1, 2}:
                # i will be 1 (for making rules with 1 item in antecedent)

                # combinations(itemset, i) generates all i-length combinations
                # For {1, 2} with i=1: combinations are (1,) and (2,)
                for antecedent in combinations(itemset, i):
                    # Convert to frozenset for dictionary lookup
                    antecedent = frozenset(antecedent)
                    # Get consequent by subtracting antecedent from itemset
                    consequent = itemset - antecedent

                    # Find antecedent's support in previous levels
                    antecedent_support = None
                    for level in freq_itemsets:
                        if antecedent in level:
                            antecedent_support = level[antecedent]
                            break

                    # Calculate confidence if antecedent found
                    if antecedent_support:
                        confidence = support / antecedent_support
                        if confidence >= min_confidence:
                            rules.append((antecedent, consequent, confidence))

    return rules


# Run the algorithm
print("Finding frequent itemsets...")
frequent_itemsets = apriori(transactions, min_support)

print("\nGenerating association rules...")
rules = generate_rules(frequent_itemsets, min_confidence)

print("\nAssociation Rules:")
for antecedent, consequent, confidence in rules:
    print(f"{set(antecedent)} -> {set(consequent)} (confidence: {confidence:.2f})")