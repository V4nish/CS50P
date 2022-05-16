# Creating our own library.....  Also saved as sayings.py for ease of import...
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")
    
def goodbye(name):
    print(f"Goodbye, {name}")


#### Now, is this program being run directly, or being called as an import???  Do we always want main() to run or only if explicity called?
#
#
#### Only call the main function if the name of this file (is main by convention) directly called.
#  try    print(__name__)     for demo

if __name__ =="__main__":
    main()
    