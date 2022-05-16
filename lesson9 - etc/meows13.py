import argparse                                             # Argument parsing library

parser = argparse.ArgumentParser(description = "Meow like a cat!")                                  # Add a description of the program
parser.add_argument("-n", default = 1, help = "Number of times to meow like a cat", type = int)     # Add description of each function (try running from command line with -h)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")