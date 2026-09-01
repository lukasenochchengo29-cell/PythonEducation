def bin_search(nums, x):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1


S = [11, 17, 26, 28, 37, 45, 53, 59]
x = int(input("Input the number to search: "))
pos = bin_search(S, x)
print(f"In S, {x} is at position {pos}.")