def calculate_gc(sequence: str) -> float:
    '''calculates the percentage of G and C in a sequence'''
    count = 0
    for x in sequence:
        if x == 'C' or x == 'G':
            count += 1

    percent_gc = 100*(count/len(sequence))

    return percent_gc

def calculate_at(sequence: str) -> float:
    '''calculates the percentage of A and T in a sequence'''
    count = 0
    for x in sequence:
        if x == 'A' or x == 'T':
            count += 1

    percent_at = 100*(count/len(sequence))

    return percent_at