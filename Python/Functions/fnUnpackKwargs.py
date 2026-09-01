def say_hi(fname, lname):
    print("Hello ", fname, lname)

def main():
    person = {"fname": "John", "lname": "Maina"}
    say_hi(**person) # Same as: say_hi(fname = "John", lname = "Maina")


if __name__ == "__main__":
    main()
