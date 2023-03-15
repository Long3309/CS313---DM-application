def apriori(transactions, min_support):
    """
    Implementation of the Apriori algorithm.
    transactions: A list of sets, where each set contains the items in a transaction.
    min_support: The minimum support threshold.
    Returns: A dictionary of itemsets and their corresponding supports.
    """
    itemsets = {}
    freq_itemsets = {}
    n = len(transactions)
    
    # Generate all 1-itemsets and their supports
    for transaction in transactions:
        for item in transaction:
            if item in itemsets:
                itemsets[item] += 1
            else:
                itemsets[item] = 1
                
    # Remove infrequent items and generate frequent 1-itemsets
    freq_itemsets[1] = {}
    for item in itemsets:
        support = itemsets[item] / n
        if support >= min_support:
            freq_itemsets[1][frozenset([item])] = support
            
    # Generate frequent itemsets of length 2 and greater
    k = 2
    while len(freq_itemsets[k-1]) > 0:
        freq_itemsets[k] = {}
        
        # Generate candidate itemsets
        candidates = generate_candidates(freq_itemsets[k-1], k)
        
        # Calculate support for each candidate itemset
        for transaction in transactions:
            for candidate in candidates:
                if candidate.issubset(transaction):
                    if candidate in freq_itemsets[k]:
                        freq_itemsets[k][candidate] += 1
                    else:
                        freq_itemsets[k][candidate] = 1
        
        # Remove infrequent itemsets and generate frequent itemsets
        for itemset in freq_itemsets[k]:
            support = freq_itemsets[k][itemset] / n
            if support >= min_support:
                freq_itemsets[k][itemset] = support
            else:
                del freq_itemsets[k][itemset]
                
        k += 1
        
    # Flatten frequent itemsets dictionary into a single dictionary
    itemset_supports = {}
    for k in freq_itemsets:
        for itemset in freq_itemsets[k]:
            itemset_supports[itemset] = freq_itemsets[k][itemset]
            
    return itemset_supports
    
def generate_candidates(itemsets, k):
    """
    Generate candidate itemsets of length k.
    itemsets: A dictionary of frequent itemsets.
    k: The length of the candidate itemsets.
    Returns: A set of candidate itemsets.
    """
    candidates = set()
    for itemset1 in itemsets:
        for itemset2 in itemsets:
            union = itemset1.union(itemset2)
            if len(union) == k and union not in candidates:
                subsets = [frozenset([item]) for item in union]
                if all(subset in itemsets for subset in subsets):
                    candidates.add(union)
    return candidates

transaction_list = ["M1, M2, M5"
"M2, M4",
"M2, M3",
"M1, M2, M4"
"M1, M3"
"M2, M3",
"M1, M3,"
"M1, M2, M3, M5"
"M1, M2, M3"]
a = apriori(transaction_list, 0.22)
print(a)
