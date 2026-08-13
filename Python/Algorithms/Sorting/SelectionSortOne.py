def main():
    numbers = [64, 25, 12, 22, 11]

    n = len(numbers)
    
    print("\nBefore Sorting:\t",numbers)

    # Traverse through all array elements
    for i in range(n - 1):
        # Assume the current position i holds the minimum element
        min_index = i
        
        # Test against the remaining unsorted elements
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
                
        
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
            
    print("\nAfter Sorting:\t",numbers)

if __name__ == "__main__":
    main()