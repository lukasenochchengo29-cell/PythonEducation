class Rectangle:
    def __init__(self):
        self.__width = 0
        self.__length = 0
        self.__area = 0
        self.__perim = 0

    def data_in(self):
        self.__width = float(input("Enter the width of the rectangle:> "))
        self.__length = float(input("Enter the length of the rectangle:> "))

    def compute(self):
        self.__area = self.__width * self.__length
        self.__perim = 2 * (self.__width + self.__length)

    def data_out(self):
        print(f"The area of the rectangle is {self.__area:.2f}")
        print(f"The perimeter of the rectangle is {self.__perim:.2f}")

def main():
    rect1 = Rectangle()

    print("Data entry for the rectangle:")
    print("----------------------------------------")
    rect1.data_in()
    rect1.compute()

    print("\nData output for the rectangle:")
    print("----------------------------------------")
    rect1.data_out()

if __name__ == "__main__":
    main()
