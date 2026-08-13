# A function that gets the larger of two numbers
def large(first, second):
   return first if first > second else second

def main():
    first = float(input("\nEnter the first number:> "))
    second = float(input("Enter the second number:> "))

    large_num = large(first, second)

    print(f"\nBetween {first} and {second} the largest is {large_num}") 

if __name__ == "__main__":
    main()