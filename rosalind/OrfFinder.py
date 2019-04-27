import sys

CODON_DICT = {
    'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
    'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
    'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
    'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
    'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
    'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
    'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def decodeCodon(codon):
    protein = None
    if len(codon) == 3 and CODON_DICT.has_key(codon):
        protein = CODON_DICT[codon]
    return protein


def reverse_complement(dna):
    lookup = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([lookup[c] for c in reversed(dna)])


def possible_protein_strings(text):
    position = []
    results = []

    l = len(text)
    for i in range(l):
        protein = decodeCodon(text[i:i + 3])
        if protein and protein == 'M':
            position.append(i)

    for i in position:
        stopCodonFoundFlag = False
        protein_string = ''

        for j in range(i, l, 3):
            protein = decodeCodon(text[j:j + 3])

            if not protein:
                break

            if protein == 'Stop':
                stopCodonFoundFlag = True
                break

            protein_string = protein_string + protein

        if stopCodonFoundFlag:
            results.append(protein_string)

    return results


if ((len(sys.argv) < 2) or (len(sys.argv) > 3)):
    print "Usage: python", sys.argv[0], "<filename> [<min ORF length]"
else:
    fileName = sys.argv[1]
    if (len(sys.argv) > 2):
        try:
            limit = int(sys.argv[2])
        except ValueError:
            print "\n\tExpecting an integer to define minimum ORF length, found ",
            print sys.argv[2]
            sys.exit(0)

    print "ORF must be atleast", limit, "Base pairs long"

    # Read the file
    with open(fileName, 'r') as f:
        # first line in fasta format describes the file
        text = f.readline().rstrip()
        print "Saw", text
        text = f.read().replace('\n', '')
        text = text.strip()

print possible_protein_strings(text)
print reverse_complement(text)
# Display the list
print "ORFs found!!"
