def main():
    name = input("What's your name? ")
    hello(name)
    
def hello(to="World"):
    print("Hello, ", to)
    
#  This works in this order, because the *main* function isn't called until after the definition of hello()

main()