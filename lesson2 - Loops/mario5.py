# Time to refactor

def main():
    print_square(3)
    
def print_square(size):
    
    # For each row in square 
    for i in range(size):
        print("#" * size)       # Busting out an old move ;)            
        print()
    
main()