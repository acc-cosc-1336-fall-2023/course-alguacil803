def get_hamming_distance(dna1, dna2):
    hamming_distance = 0
    if len(dna1) != len(dna2):
        return "Invalid, both strings are not of equal length"
    else:
        for position in range(len(dna1)):
            if dna1[position] != dna2[position]:
                hamming_distance += 1
        return hamming_distance
    
def get_dna_complement(dna):
    verify = verify_if_dna(dna)
    if verify == "DNA":
        complement = dna.replace("A", "t"). replace("T","a").replace("C","g").replace("G","c")
        reverse_complement = complement [::-1]
        reverse_complement = reverse_complement.upper()
        return reverse_complement
    return verify    

def verify_if_dna(dna):
    count = 0
    if dna == '':
        return "This is not a DNA strand."
    for i in range(len(dna)):
        if (dna[i] == 'A' or dna[i] == 'G' or dna[i] == 'C' or dna[i] == 'T'):
            count += 1
    if count != len (dna):
        return "This is not a DNA strand."
    else:
        return "DNA"
    

    
    