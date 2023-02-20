gene1 = "STE11"
gene2 = "BRCA1"
gene3 = "p53"
print(gene1)
print(gene2)
print(gene3)

# lists
#               0    ,   1   ,   2
gene_list = ["STE11", "BRCA1", "p53"]
gene_list = [1, 2]
gene_list[0] = 5
gene_list.append(7)
print(type(gene_list))
gene_of_interest = gene_list[1]
print(gene_list)
is_in_list = 6 in gene_list
print(is_in_list)
gene_list.sort()
print(gene_list)
