"""
How many calculations do I have to do on average until I get the sequence?
What happens if I add a new protein id?
"""

protein_ids = ["Ste11", "Bem1", "p53"]
protein_seqs = ["ACGT", "WERT", "DERT"]

for index, protein_id in enumerate(protein_ids):
    if protein_id == "p53":
        print(protein_seqs[index])
