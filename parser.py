
def parse_fasta(filename):
    results = []
    header = None
    sequence_parts = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith('>'):
                if header is not None:
                    results.append((header, ''.join(sequence_parts)))
                header = line
                sequence_parts = []
            else:
                sequence_parts.append(line)

    if header is not None:
        results.append((header, ''.join(sequence_parts)))

    return results






