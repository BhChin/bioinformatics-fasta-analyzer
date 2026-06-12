def sequence_length(sequence: str) -> int:
    return len(sequence)

def reverse_sequence(sequence: str) -> str:
    return sequence[::-1]

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


def count_nucleotides(sequence: str) -> dict:
    '''counts nucleotides of a sequence'''

    a = sequence.count('A')
    t = sequence.count('T')
    c = sequence.count('C')
    g = sequence.count('g')

    nucleotide = {'A': a, 'T': t, 'C': c, 'G': g}

    return nucleotide

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

def complement(sequence: str, type: str) -> str:
    if type == 'DNA':
        return dna_complement(sequence)
    else: # rna
        return rna_complement(sequence)

def dna_complement(sequence: str) -> str:
    sequence_list = list(sequence)
    for x in range(len(sequence_list)):
        if sequence_list[x] == 'C':
            sequence_list[x] = 'G'
        elif sequence_list[x] == 'G':
            sequence_list[x] = 'C'
        elif sequence_list[x] == 'A':
            sequence_list[x] = 'T'
        elif sequence_list[x] == 'T':
            sequence_list[x] = 'A'
    result = ''.join(sequence_list)
    return result

def rna_complement(sequence: str) -> str:
    sequence_list = list(sequence)
    for x in range(len(sequence_list)):
        if sequence_list[x] == 'C':
            sequence_list[x] = 'G'
        elif sequence_list[x] == 'G':
            sequence_list[x] = 'C'
        elif sequence_list[x] == 'A':
            sequence_list[x] = 'U'
        elif sequence_list[x] == 'U':
            sequence_list[x] = 'A'

    result = ''.join(sequence_list)
    return result

def reverse_complement(sequence: str, type: str) -> str:
    '''returns the reverse complement of a sequence'''
    if not sequence:
        return ''

    sequence = reverse_sequence(sequence)
    return complement(sequence, type )