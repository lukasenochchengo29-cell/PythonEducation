def bin(n, k):
    B = [[0] * (i + 1) for i in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]

    return B[n][k]
    

def main():
    n = int(input("\nInput the value of n: "))
    k = int(input("Input the value of k: "))
 
    print(f"\nbinomial({n}, {k}) is {bin(n,k)}")

if __name__ == "__main__":
    main()
       