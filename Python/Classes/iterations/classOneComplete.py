class Employee:
    def __init__(self, name = "", age = 0):
        self.__name =  name
        self.__age = age

    def data_in(self):
        self.__name =  input("Enter the employee\'s name -> ")
        self.__age = float(input("Enter the employee\'s age -> "))

    def data_out(self):
        print(f"Employee's name: {self.__name}")
        print(f"Employee\'s age: {self.__age}")

def main():
    emp1 = Employee("Pauline Moraa",32)
    emp2 = Employee()

    print("\nAnalysis for employee 1 (first time):")
    print("------------------------------------");
    emp1.data_out()

    print("\nAnalysis for employee 2 (first time):")
    print("------------------------------------")
    emp2.data_out()

    print("\nData input for employee 1:")
    print("------------------------------------");
    emp1.data_in()

    print("\nData input for employee 2: ")
    print("------------------------------------")
    emp2.data_in()

    print("\nAnalysis for employee 1 (second time):")
    print("------------------------------------");
    emp1.data_out()

    print("\nAnalysis for employee 2 (second time):")
    print("------------------------------------")
    emp2.data_out()

if __name__ == "__main__":
    main()