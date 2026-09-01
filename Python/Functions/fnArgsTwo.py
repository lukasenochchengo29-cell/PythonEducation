def display_students(*students):
  print("\nThe students are:")
  for the_student in students:
    print(the_student, end = " ")

def main():
  display_students("Alice", "Jane", "John", "Tom", "Lukas", "Enock", "Melchizedek")

if __name__ == "__main__":
  main()