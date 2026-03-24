import unittest
import tempfile
from parser import parse_fasta

class TestParser(unittest.TestCase):
    def setUpTestFile(self):
        pass



    def test_parse_fasta(self):

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as my_temp_file:
            my_temp_file.write('>Apple\n')
            my_temp_file.write('CCCCTTTTAAAAGGGG\n')
            filename = my_temp_file.name


            self.assertEqual(parse_fasta(filename), [('>Apple', 'CCCCTTTTAAAAGGGG')])







