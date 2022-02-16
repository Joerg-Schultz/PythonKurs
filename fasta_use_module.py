import fasta_parser_module as f_parser

seqs = f_parser.fasta_parser("sequences.fasta")
for (key, value) in seqs.items():
    print(f"id: {key}\n{value}")
