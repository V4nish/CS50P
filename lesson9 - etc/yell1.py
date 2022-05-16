def main():
    yell(["This", "is", "CS50"])
    

def yell(words):
    for word in words:
        print(word, end=" ")
    

if __name__ == "__main__":
    main()