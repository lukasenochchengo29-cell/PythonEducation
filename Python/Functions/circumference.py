import math
circumference = lambda radius : 2 * math.pi * radius
area = lambda radius : math.pi * radius * radius


def main():
    radii = float(input("Enter radius: "))
    print(f"The circumference is: {circumference(radii):.2f}")
    print(f"The area is: {area(radii):.2f}")  

if __name__ == "__main__":
    main()