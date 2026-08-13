def main():
    city = ["Nairobi", "Kisumu", "Nakuru", "Thika", "Mombasa"]
    
    sorted_cities = sorted(city, key = lambda x : len(x),reverse = True)
    
    print(sorted_cities)
    
if __name__ == "__main__":
    main()
