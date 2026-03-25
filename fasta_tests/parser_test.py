import unittest
import tempfile
from parser import parse_fasta

class TestParser(unittest.TestCase):
    def test_parse_fasta(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=True) as my_temp_file:
            my_temp_file.write('>Apple\n')
            my_temp_file.write('CCCCTTTTAAAAGGGG\n')

            # didn't have this previously which caused my test to fail
            #flush(): "forces any data that is waiting in an internal
            #memory buffer to be immediately written to its destination"
            my_temp_file.flush()

            filename = my_temp_file.name
            self.assertEqual(parse_fasta(filename),
                             [('>Apple', 'CCCCTTTTAAAAGGGG')])