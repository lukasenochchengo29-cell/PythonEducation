def get_large(*numbers):
  if len(numbers) == 0:
    return None

  max_num = numbers[0]

  for num in numbers:
    if num > max_num:
      max_num = num


  return max_num

def main():
  num1 = float(input("\nEnter the first number:> "))
  num2 = float(input("Enter the second number:> "))
  num3 = float(input("Enter the third number:> "))
  num4 = float(input("Enter the fourth number:> "))


  print(f"\nWith no vaues, the largest is {get_large()}")
  print(f"Between {num1} and {num2} the largest is {get_large(num1,num2)}")
  print(f"Among {num1}, {num2} and {num3} the largest is {get_large(num1,num2,num3)}")
  print(f"Among {num1}, {num2}, {num3} and {num4} the largest is {get_large(num1,num2,num3,num4)}")

if __name__ == "__main__":
   main()
