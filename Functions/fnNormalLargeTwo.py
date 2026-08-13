# A function that gets the larger of two numbers
def large(first, second):
   if first > second :
     return first
   else :
     return second

def main():
    first = float(input("\nEnter the first number:> "))
    second = float(input("Enter the second number:> "))

    large_num = large(first, second)

    print(f"\nBetween {first} and {second} the largest is {large_num}") 

if __name__ == "__main__":
    main()