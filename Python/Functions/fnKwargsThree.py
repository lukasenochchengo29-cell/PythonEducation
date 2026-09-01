def display(**myvar):
    print("Type:\t\t", type(myvar))
    print("Name:\t\t", myvar["name"])
    print("Age:\t\t", myvar["age"])
    print("All data:\t", myvar)

def main():
    display(name = "John", age = 26, gender = "Male", city = "Nairobi")

if __name__ == "__main__":
    main()
