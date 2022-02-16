
cutoff = 0.01

significant_genes = {}
with open("data/cor_vs_trap.csv", "r") as diff_expr:
    for full_line in diff_expr:
        line = full_line.rstrip("\n")
        values = line.split(',')
        gene, logfold, p_value = (values[0], values[2], values[6])
        gene = gene.replace("\"", "")
        if not gene or logfold == "NA" or p_value == "NA":
            continue
        if float(logfold) > 0 and float(p_value) <= cutoff: # I don't have to declare types, but then have to convert it???
            significant_genes[gene] = float(p_value), float(logfold)

print("Found " + str(len(significant_genes.keys())) + " upregulated genes")

significant_kinases = {}
with open("data/Dm_Interproscan.tsv", "r") as interpro:
    for full_line in interpro: # There is no fucking scope????
        values = full_line.split("\t")
        gene, database, description = (values[0], values[3], values[5])
        gene = gene.replace("-RA","")
        if database != "Pfam": continue
        if not ("kinase" in description): continue
        if gene in significant_genes:
            significant_kinases[gene] = 1

print("Kinases " + str(len(significant_kinases.keys())))