# A function that doubles a number
make_double = lambda num: num * 2

def main():
    the_value = float(input("\nEnter a number:> "))
    print(f"\nIf you double {the_value} you get ", make_double(the_value)) 

if __name__ == "__main__":
    main()