def display(the_country, *args, **kwargs):
    print("Regular:\t\t", the_country)
    print("Positional arguments:\t", args)
    print("Keyword arguments:\t", kwargs)

def main():
    display("Kenya", "John Maina", 26, gender = "Male", city = "Nairobi")

if __name__ == "__main__":
    main()
