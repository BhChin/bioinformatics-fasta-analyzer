from calculation import *
class Sequence:
    def __init__(self, header, sequence):
        self._header = header[1:]
        self._sequence = sequence

    def sequence(self):
        return self._sequence

    def header(self):
        return self._header

    def sequence_length(self):
        return len(self._sequence)

    def gc_content(self):
        '''returns the percentage of G and C'''
        return calculate_gc(self._sequence)




