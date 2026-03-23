
def parse_fasta(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            print(line.strip())