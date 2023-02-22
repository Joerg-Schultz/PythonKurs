#######
# The for loop
######
for my_counting_variable in range(3,5):
    print("Hello")
    print("World")

gene_list = ["STE11", "BRCA1", "p53", "MYC", "p53"]
for gene in gene_list:
    print(f"The current gene is {gene}")

print("I looked at each gene")

# in which position of the gene_list is the gene
# with the identifier p53?

# go through the elements of the list beginning with the first and remember the position
# then for each of the elements check whether it is equal to p53

position = 0
for gene in gene_list:
    # Code belonging to 'for' loop:
    print(f"The current gene is {gene} and it is in position {position}")
    position += 1  # this is the same as position = position + 1

    # We have to increase the position variable by one now!
    # end of code
print("Finished")


search_gene = "p53"
for position in range(0, len(gene_list)):
    if gene_list[position] == search_gene:
        print(position, gene_list[position])

counter = 0
for gene in gene_list:
    if gene == search_gene:
        print(counter, gene)
    counter += 1

for idx, gene in enumerate(gene_list):
    if gene == search_gene:
        print(idx + 1, gene)

# Careful breaks if not in list
# Only reports first element
print(gene_list.index(search_gene) + 1)

#####
# While Loop
#####
print("Here starts the while loop section")
running = True
while running:
    print("Hallo")
    running = False
print("Stopped while Loop")

# rewrite
# in which position of the gene_list is the gene
# with the identifier p53?
# Now with while
gene_list = ["STE11", "BRCA1", "p53", "MYC", "p53"]

counter = 0
while counter < len(gene_list):
    gene = gene_list[counter]
    if gene == "STE11":  #  Print position if gene == p53
        print(gene, counter)
    counter += 1

print("Done")

#### Exercise
gene_names = ["STE11", "BRCA1", "p53", "MYC"]
#               |         |       |      |
gene_length = [123,      56,     254,   321]
# Write a program that reports the length for a gene given the name
query = "BRCA1"  #  -> 56
for pos, gene in enumerate(gene_names):
    print(pos, gene)
    if gene == "p53":
        length = gene_length[pos]
        print(f"Length = {length}")

