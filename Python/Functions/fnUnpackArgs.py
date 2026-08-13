def get_sum(first, second, third):
    return first + second + third

def main():
    numbers = [10, 20, 30]
    sum = get_sum(*numbers) # Same as: get_sum(10, 20, 30)

    print(f"\nThe sum is {sum}\n")

if __name__ == "__main__":
    main()