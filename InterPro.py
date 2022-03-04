class Domain:

    def __init__(self, pfamID, description):  # constructor
        self.db_identifier = pfamID
        self.function = description


class Protein:

    def __init__(self, identifier):
        self.id = identifier
        self.domain_list = []

    def add_domain(self, domain):
        self.domain_list.append(domain)


domain_dictionary = {}
protein_dictionary = {}
with open("c:/Users/Joerg/Downloads/Dm_Interproscan.tsv", "r") as interpro:
    for line in interpro:
        columns = line.split("\t")
        gene_identifier, database, db_identifier, function = (
            columns[0], columns[3], columns[4], columns[5])  # columns[0,3,5] Perl style :P columns[1..4]
        if database == "Pfam":
            if gene_identifier not in protein_dictionary:
                new_protein = Protein(identifier=gene_identifier)
                protein_dictionary[gene_identifier] = new_protein
            if db_identifier not in domain_dictionary.keys():
                domain_dictionary[db_identifier] = Domain(pfamID=db_identifier, description=function)
            protein_dictionary[gene_identifier].add_domain(domain_dictionary[db_identifier])

print(f"We found {len(domain_dictionary.keys())} domains!")
print(f"We found {len(protein_dictionary.keys())} proteins!")

# maximal number of domains in a protein
max_domain_count = 0
for protein in protein_dictionary.values():
    number_of_domain = len(protein.domain_list)
    if number_of_domain > max_domain_count:
        max_domain_count = number_of_domain
print(f"Maximal domain count for all proteins: {max_domain_count}")




