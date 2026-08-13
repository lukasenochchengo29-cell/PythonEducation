def main():
    # Sort coordinates by their Y value (the second element)
    points = [(5, 12), (8, 9), (1, 4), (22, 2), (3, 7)]

    sorted_points = sorted(points, key = lambda point : point[1])

    print(sorted_points)  # Output: [(22, 2), (1, 4), (3, 7), (8, 9), (5, 12)]
    
if __name__ == "__main__":
    main()
