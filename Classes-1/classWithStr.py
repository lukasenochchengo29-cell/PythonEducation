class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

def main():
    emp1 = Employee("Patrick Otieno",45)
    
    print(emp1);

if __name__ == "__main__":
    main()