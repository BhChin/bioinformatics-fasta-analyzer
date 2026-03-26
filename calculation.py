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

def find_codons(sequence: str) -> dict:
    '''finds 3-mer sequences of a sequence'''
    codons = {}
    for x in range(len(sequence) - 2):
        if sequence[x:x + 3] not in codons:
            codons[sequence[x:x + 3]] = 1
        else:
            codons[sequence[x:x + 3]] += 1

    return codons

def find_dimers(sequence: str) -> dict:
    '''finds 2-mer sequences of a sequence'''
    dimers = {}
    for x in range(len(sequence)-1):
        if sequence[x:x+2] not in dimers:
            dimers[sequence[x:x+2]] = 1
        else:
            dimers[sequence[x:x+2]] += 1

    return dimers

