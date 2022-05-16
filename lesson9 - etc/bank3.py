## UnboundLocalError: local variable 'balance' referenced before assignment

balance = 0                                # a global variable

def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    
def deposit(n):
    balance += n
    
def withdraw(n):
    balance -= n
    
if __name__ == "__main__":
    main()