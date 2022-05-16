# Creating our own library.....
def main():
    hello("world")
    goodbye("world")
    
def hello(name):
    print(f"Hello, {name}")
    
def goodbye(name):
    print(f"Goodbye, {name}")
  
# Only run the main() function if the filename is main, so main doesn't run when it is imported.
if __name__ == "__main__":
    main()  