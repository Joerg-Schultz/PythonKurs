"""
Read in a fasta formatted file
store the content in a dictionary with ids as key and sequence as values
run through the dictionary and print the ids plus the sequences
"""

protein_seq = ""
protein_id = ""
result = {}
with open("sequences.fasta", "r") as fasta_file:
    for full_line in fasta_file:
        line = full_line.rstrip('\n')  # Contrasting chomp, rstrip does not change line
        if line[0] == '>':
            if protein_id: # empty string is false
                result[protein_id] = protein_seq
            protein_seq = ""
            protein_id = line[1:]
        else:
            protein_seq += line
    result[protein_id] = protein_seq

for (key, value) in result.items():
    print(f"id: {key}\n{value}")
