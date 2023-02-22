gene2length = {
    "STE11": 123,  # key : value
    "BRAC1": 56,
    "p53": 254,
    "Myc": 321,
}

#
# test_dictionary = {
#    "MOUSE": {"genecount": 23, "genomelength": "3GBp", "genes": ["bla", "blub"]},
#     "HUMAN": {"genecount": 25, "genomelength": "3GBp"}
# }

# words as indices
query = "STE11"
length = gene2length[query]
print(f"The gene {query} has the length {length}")

gene2length["bla"] = 234  # add a new key value pair
#gene2length = {"bla": 234}  # store a new dictionary
print(gene2length)

gene_names = gene2length.keys()
print(gene_names)
gene_length = gene2length.values()
print(gene_length)
