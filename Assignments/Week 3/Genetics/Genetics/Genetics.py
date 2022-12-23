def verifyGene(gene):
    genes = []
    end = ["TAG", "TAA", "TGA"]
    cannotcontain = ["ATG", "TAG", "TAA", "TGA"]
    currentgene = ""
    status = False
    for i in range(0, len(gene)):
        currentgene = gene[i:(i+3)]
        if i < len(gene) - 3 and currentgene == "ATG":
            for j in range(i + 3, len(gene)):
                if j < len(gene) - 3 and gene[j:(j+3)] in end:
                    if gene[(i+3):j] not in cannotcontain:
                        status = True
                        genes.append(gene[(i+3):j])
    if status == False and len(genes) == 0:
        print("no gene is found")
    else:
        for i in genes:
            print(i)

def main():
    genome = input("Enter a genome string: ")
    verifyGene(genome.toupper())

if __name__ == "__main__":
    main()

