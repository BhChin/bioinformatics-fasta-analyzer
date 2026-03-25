from parser import parse_fasta

def main():

    sequences = parse_fasta('mus-musculus-hemoglobin.fasta')
    print(sequences)











if __name__ == '__main__':
    main()