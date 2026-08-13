def main():
    numbers = [1, 2, 3, 4]

    squared = list(map(lambda x : x ** 2, numbers))

    print(squared)  # Output: [1, 4, 9, 16]

if __name__ == "__main__":
    main()
