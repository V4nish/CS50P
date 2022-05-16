import sys

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# Print name tags
for arg in sys.argv[1:]:       # Slices list - start at location 1 then continue to end
    print("Hello, my name is", arg)