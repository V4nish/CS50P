import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("newStudents.csv", "a", newline='') as file:                # The newline bit is for Windows only to stop an additional emtpy line per input
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])      # Try: Number 4, Privet Drive
    writer.writerow({"name":name, "home": home})