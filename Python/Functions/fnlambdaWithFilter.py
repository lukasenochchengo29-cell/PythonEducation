def main():
    numbers = [13, 26, 30, 41, 58, 63]

    evens = list(filter(lambda x : x % 2 == 0, numbers))

    print(evens)  # Output: [26,30, 58]

if __name__ == "__main__":
    main()
