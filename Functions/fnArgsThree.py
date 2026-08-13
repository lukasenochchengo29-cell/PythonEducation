def display_students(*args):
  print("Type: ",type(args))
  print("First: ", args[0])
  print("Second: ", args[1])
  print("Third: ", args[2])
  print("Fourth: ", args[3]) 

def main():
  display_students("Alice", "Jane", "John", "Tom")

if __name__ == "__main__":
  main()