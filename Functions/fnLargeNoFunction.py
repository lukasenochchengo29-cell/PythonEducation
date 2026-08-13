

def main():
    first = float(input("\nEnter the first number:> "))
    second = float(input("Enter the second number:> "))

    large_num = first if first > second else second

    print(f"\nBetween {first} and {second} the largest is {large_num}") 

if __name__ == "__main__":
    main()