# A function that checks if a number is even
is_even = lambda number : True if number % 2 == 0 else False

def main():
    my_number = float(input("\nEnter a number:> "))

    print(f"\nIs {my_number} even? ", is_even(my_number)) 

if __name__ == "__main__":
    main()