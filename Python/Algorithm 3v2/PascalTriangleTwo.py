def bin(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return bin(n - 1, k - 1) + bin(n - 1, k)

def main():
    n = int(input("\nEnter the number of rows: "))

    for i in range(n + 1):
        print("  " * (n - i), end = "")
        for j in range(i + 1):
            print(f"  {bin(i,j)}" , end = " ")
        print()        

if __name__ == "__main__":
    main()
       