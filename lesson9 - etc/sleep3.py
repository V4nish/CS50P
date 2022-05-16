def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)
        
def sheep(n):
    for i in range(n):
        yield "🐑" * (i + 1)                        # A million+ is fine now :)  Yeild generator is returning one at a time.
        
if __name__ == "__main__":
    main()