def find_k_mers(dna_sequence, k):
    k_mers_file = open('kmers.txt', 'a+')
    for i in range(len(dna_sequence) - k + 1):
        kmer_dictionary = dict()
        kmer = dna_sequence[i:i + k]
        # count how many times the kmer appears in the dna_sequence, and then associate that count with the kmer
        # in kmer_dictionary
        kmer_dictionary[kmer] = dna_sequence.count(kmer)
        #if the kmer appears more than once, write it to k_mers_file
        if kmer_dictionary[kmer] > 1:
            print(kmer_dictionary)
            k_mers_file.write(kmer + '\n')
    k_mers_file.close()

def main():
    # open 'dna.txt' in read mode
    dna_file = open('dna.txt', 'r')
    # read the file
    dna = dna_file.read()
    # close the file
    dna_file.close()
    # find k-mers of length at least 5 that appear more than once
    new_dna = dna.replace('\n', '')
    max_kmer_length = len(new_dna) // 2
    for i in range(5, max_kmer_length):
        find_k_mers(new_dna, i)

if __name__ == "__main__":
    main()