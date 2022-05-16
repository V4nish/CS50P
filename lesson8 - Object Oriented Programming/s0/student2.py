def main():
    name = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")    ## OK, so how can we solve this as we can only return one value?!?!?!

if __name__ == "__main__":
    main()
