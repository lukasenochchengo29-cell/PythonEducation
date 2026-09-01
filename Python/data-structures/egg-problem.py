from random import randint

def do_experiment(floor, breaking):
    return floor >= breaking

def find_highest_safe_floor(height, breaking):
    for n in range(1, height + 1):
        if do_experiment(n, breaking):
            return n - 1
    return height

height = int(input("Input the number of floors: "))
breaking = randint(1, height)
floor = find_highest_safe_floor(height, breaking)
print(f"Your egg will safe till the {floor}-th floor.")