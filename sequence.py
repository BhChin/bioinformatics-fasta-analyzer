from calculation import *
class Sequence:
    def __init__(self, header, sequence):
        self._header = header
        self._sequence = sequence

    def __repr__(self): # representation for developer
        return f"Sequence({self._header}: {self._sequence})"

    def __str__(self): # user-friendly representation
        return f"{self._header}: {self._sequence}"

    def sequence(self):
        return self._sequence

    def header(self):
        return self._header

    def sequence_length(self):
        '''returns length of the sequence'''
        return sequence_length(self._sequence)

    def nucleotides(self):
        '''returns dictionary of nucleotides of a sequence'''
        return count_nucleotides(self._sequence)

    def gc_content(self):
        '''returns the percentage of G and C'''
        return calculate_gc(self._sequence)

    def at_content(self):
        '''returns the percentage of A and T'''
        return calculate_at(self._sequence)

    def dimers(self):
        '''returns a sequences' dimers'''
        return find_dimers(self._sequence)

    def codons(self):
        '''returns a sequences' codons'''
        return find_codons(self._sequence)





