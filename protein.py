class Domain:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        # Use this to explain encapsulation.
        # add the length parameter without touching the protein class
        # length = self.end - self.start + 1
        # return f"{self.name}: {self.start}-{self.end} ({length} AA)"
        return f"{self.name}: {self.start}-{self.end}"


class Protein:
    def __init__(self, db_identifier, domains=None):
        if domains is None:
            domains = []
        self.db_identifier = db_identifier
        self.domains = domains

    def __str__(self):
        # To return a new list, use the sorted() built-in function...
        # newlist = sorted(ut, key=lambda x: x.count, reverse=True)
        # You could change the sort to sort by length
        domain_string = ', '.join([str(domain) for domain in sorted(self.domains, key=lambda x: x.start)])
        # domain_string = ', '.join([str(domain) for domain in sorted(self.domains, key=lambda x: x.end - x.start)])
        return f"{self.db_identifier}: {domain_string}"

    def add_domain(self, domain):
        self.domains.append(domain)


sh3 = Domain("SH3", 7, 95)
p53 = Protein("p53_HUMAN", [Domain("PH", 204, 295)])
sh2 = Domain("SH2", 105, 197)
print(sh2)
p53.add_domain(sh2)
p53.add_domain(sh3)
print(p53)
