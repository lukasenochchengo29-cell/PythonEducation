class Rectangle:
    def __init__(self, width = 0, length = 0):
        self.__width = width
        self.__length = length
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
    rect1 = Rectangle(10,20)
    rect2 = Rectangle()

    print("\nData output for rectangle 1 (first time):")
    print("--------------------------------------------------")
    rect1.compute()
    rect1.data_out()

    print("\nData output for rectangle 2 (first time):")
    print("--------------------------------------------------")
    rect2.compute()
    rect2.data_out()

    print("\nData entry for rectangle 1:")
    print("--------------------------------------------------")
    rect1.data_in()
    rect1.compute()

    print("\nData entry for rectangle 2:")
    print("--------------------------------------------------")
    rect2.data_in()
    rect2.compute()

    print("\nData output for rectangle 1 (second time):")
    print("--------------------------------------------------")
    rect1.data_out()

    print("\nData output for rectangle 2:")
    print("--------------------------------------------------")
    rect2.data_out()

if __name__ == "__main__":
    main()
