def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Before swapping: num1 =", num1, ", num2 =", num2)

    num1, num2 = num2, num1

    print("After swapping: num1 =", num1, ", num2 =", num2)


if __name__ == "__main__":
    main()