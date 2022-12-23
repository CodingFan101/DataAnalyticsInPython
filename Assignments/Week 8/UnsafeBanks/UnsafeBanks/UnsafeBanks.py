import numpy as np
def main():
    try:
        # Read input
        n, limit = [int(x) for x in input().split()]
        # Define an array of float numbers using numpy
        borrowers = np.zeros((n,n), dtype = np.float64)
        result = "Unsafe banks are "
        col_index = 0
        unsafebanks = []
        for i in range(n):
            currentline = [float(x) for x in input().split()]
            balance = currentline[0]
            borrowers[i][col_index] = balance
            banks_borrowed = currentline[1]
            pairs = map(float, currentline[2:len(currentline)])
            pairs_list = list(pairs)
            if banks_borrowed != len(pairs_list)/2:
                print("Invalid input")
                exit()
            for m in range(0, len(pairs_list) - 1, 2):
               j_index = int(pairs_list[m])
               amount_owed = pairs_list[m+1]
               borrowers[i][j_index] += amount_owed
            col_index += 1
        new_index = 0
        for i in range(n):
            sum = borrowers[i].sum()
            if sum < limit:
                unsafebanks.append(i)
                new_index = (i+i) % n
                borrowers[new_index][i] = 0
                if (borrowers[new_index].sum() < limit):
                    unsafebanks.append(new_index)   
        for i in unsafebanks:
            result += str(i) + " "
        print(result)
    except ValueError:
       print("Invalid input")
       exit()
            
if __name__ == "__main__":
    main()