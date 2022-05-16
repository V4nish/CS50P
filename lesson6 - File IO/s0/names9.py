with open("names.txt", "r") as file:        # 
    for line in file:                       # such a subtle change ;)
        print("hello, ", line.rstrip())   

## Elegant!  But now we can't sort, which is why sometimes we may need the slightly more onerous method.