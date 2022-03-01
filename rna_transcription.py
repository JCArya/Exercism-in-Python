def to_rna(dna_strand):
    new_dna_strand = ""
    for element in dna_strand:
        if element == "G":
            new_dna_strand += "C"
        elif element == "C":
            new_dna_strand += "G"
        elif element == "T":
            new_dna_strand += "A"
        else:
            new_dna_strand += "U"
    return new_dna_strand
