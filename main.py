from parser import parse_fasta

def main():

    #idea 1
    #create class representing each individual sequence
    #which will have callable methods such as GC content



    sequences = parse_fasta('mus-musculus-hemoglobin.fasta')
    print(sequences)











if __name__ == '__main__':
    main()