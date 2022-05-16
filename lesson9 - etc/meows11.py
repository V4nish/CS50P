import sys                                                  # Command prompt version

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv)  == 3 and sys.argv[1] == "-n":             # Number of meows 
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")