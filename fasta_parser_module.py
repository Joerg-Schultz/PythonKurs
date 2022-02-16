
def fasta_parser(file):
    """

    :param file: fasta formatted text file
    :return: Dictionary with keys seqs id and value sequence
    """
    protein_seq = ""
    protein_id = ""
    result = {}
    with open(file, "r") as fasta_file:
        for full_line in fasta_file:
            line = full_line.rstrip('\n')  # Contrasting chomp, rstrip does not change line
            if line[0] == '>':
                if protein_id:  # empty string is false
                    result[protein_id] = protein_seq
                protein_seq = ""
                protein_id = line[1:]
            else:
                protein_seq += line
        result[protein_id] = protein_seq
    return result
