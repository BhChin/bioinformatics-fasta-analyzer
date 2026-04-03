from parser import parse_fasta

def main():

    #idea 1
    #create class representing each individual sequence
    #which will have callable methods such as GC content

    #wtd
    #calculate individual dna sequence stats
    #1. gc_content
    #2. at_content
    #3 sequence length
    #4 nucleotide frequency (probably use a dict)
    #5 codon frequency
    #

    #calculate comparable stats between different dna sequences

    while True:
        fasta_path = input('Fasta Path: ')


        if a == 'End':
            break

    sequences = parse_fasta('fasta_files/mus-musculus-hemoglobin.fasta')
    print(sequences)












if __name__ == '__main__':
    main()