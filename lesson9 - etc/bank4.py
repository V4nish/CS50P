## UnboundLocalError: local variable 'balance' referenced before assignment
# So the global variable can be read from anywhere, but not written to

def main():
    balance = 0                                # a global variable to this function??????
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    
def deposit(n):
    balance += n
    
def withdraw(n):
    balance -= n
    
if __name__ == "__main__":
    main()