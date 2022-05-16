name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close

# Now run this code three times, adding three names.