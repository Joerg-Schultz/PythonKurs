from Bio import SeqIO

longest = 0

for record in SeqIO.parse("sequences.fasta", "fasta"):
    print(record.id)
    print(len(record.seq))
    if len(record.seq) > longest:
        longest = len(record.seq)

print(longest)