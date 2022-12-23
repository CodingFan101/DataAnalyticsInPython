def verifyGenome(genome):
    genes = []
    list1 = []
    list2 = []
    start = "ATG"
    end = ["TAG", "TAA", "TGA"]
    for i in range(len(genome)):
        if genome.startswith(start, i):
            list1.append(i)
        elif genome.startswith(end[0], i):
            list2.append(i)
        elif genome.startswith(end[1], i):
            list2.append(i)
        elif genome.startswith(end[2], i):
            list2.append(i)
    for i in list1:
        for j in list2:
            if((j - (i + 3)) % 3) == 0:
                genes.append(genome[i+3:j])
    if len(genes) == 0:
        print("no gene is found")
    else:
        for i in genes:
            print(i)

def main():
    genome = input("Enter a genome string: ")
    verifyGenome(genome.upper())

if __name__ == "__main__":
    main()
