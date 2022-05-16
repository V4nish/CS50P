def main():
    n = int(input("What's n? "))
    for i in range(n):
        print(sheep(i))
        
def sheep(n):
    return "🐑" * (n + 1)
        
if __name__ == "__main__":
    main()