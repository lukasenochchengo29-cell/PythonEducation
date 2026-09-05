def bin(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return bin(n - 1, k - 1) + bin(n - 1, k)

def main():
    n = int(input("\nInput the value of n: "))
    k = int(input("Input the value of k: "))
 
    print(f"\nbinomial({n}, {k}) is {bin(n,k)}")

if __name__ == "__main__":
    main()
       