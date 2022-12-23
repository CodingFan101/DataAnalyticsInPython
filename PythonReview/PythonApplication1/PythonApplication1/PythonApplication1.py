
def test():
    
    A = [1, 2, 3, 4, 5]
    for i in range(0, 5, 1):
        if A[i] % 2 == 0:
            print(A[i])
        else:
            continue
        
def main(): 
    test()

if __name__ == "__main__":
    main()