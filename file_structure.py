class Sequence:
    def __init__(self, header, sequence):
        self._header = header[1:]
        self._sequence = sequence

    def sequence(self):
        return self._sequence

    def header(self):
        return self._header

    def gc_content(self):
        '''returns amount of G and C in a sequence'''
        count = 0
        for x in self._sequence:
            if x == 'C' or x == 'G':
                count +=1

        return count/2



