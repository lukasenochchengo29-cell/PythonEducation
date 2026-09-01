def main():
    students = [("Otieno", 23), ("Moraa", 24), ("Abdalla", 25), ("Kariuki", 22)]

    sorted_students = sorted(students, key = lambda x : x[1])

    print(sorted_students)
    
if __name__ == "__main__":
    main()
