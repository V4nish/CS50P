def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)
        
def sheep(n):                                       # Run with a million sheep and run out of memory!
    flock = []
    for i in range(n):
        flock.append("🐑" * (i + 1))
    return flock                                    # Returns the WHOLE flock at once!
        
if __name__ == "__main__":
    main()