# A function that gets the larger of two numbers
large = lambda num1, num2 : num1 if num1 > num2 else num2

def main():
    first = float(input("\nEnter the first number:> "))
    second = float(input("Enter the second number:> "))

    large_num = large(first,second)

    print(f"\nBetween {first} and {second} the largest is {large_num}") 

if __name__ == "__main__":
    main()