def get_sum(*numbers):
  total = 0
  for num in numbers:
    total = total + num
  return total

def main():
  num1 = float(input("\nEnter the first number:> "))
  num2 = float(input("Enter the second number:> "))
  num3 = float(input("Enter the third number:> "))
  num4 = float(input("Enter the fourth number:> "))

  print(f"\n{num1} + {num2} = {get_sum(num1,num2)}")
  print(f"{num1} + {num2} + {num3} = {get_sum(num1,num2,num3)}")
  print(f"{num1} + {num2} + {num3} + {num4} = {get_sum(num1,num2,num3,num4)}")

if __name__ == "__main__":
   main()
