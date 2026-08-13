# A function that adds two numbers
add = lambda num1, num2 : num1 + num2

def main():
    first = float(input("\nEnter the first number:> "))
    second = float(input("Enter the second number:> "))

    sum = add(first,second)

    print(f"\n{first} + {second} = {sum}") 

if __name__ == "__main__":
    main()