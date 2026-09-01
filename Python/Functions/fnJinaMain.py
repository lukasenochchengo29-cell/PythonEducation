def greetings_function(jina): # name is a parameter
  print("\nHello ", jina)

def main():
  name = input("\nEnter your name: ")
  greetings_function(name) #name is an argument

if __name__ == "__main__":
  main()
