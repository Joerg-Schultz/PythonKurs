import db_functions.fasta_parser_module
import db_functions.fasta_parser_module as f_parser

seqs = db_functions.fasta_parser_module.fasta_parser("sequences.fasta")
seqs2 = f_parser.fasta_parser("sequences.fasta")