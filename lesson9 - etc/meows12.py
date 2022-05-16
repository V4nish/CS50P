import argparse                                             # Argument parsing library

parser = argparse.ArgumentParser()                          # Create a new parser instance
parser.add_argument("-n")                                   # Add the optional arguments
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")