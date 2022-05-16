def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house               # Not all languages support this.  A tuple!  Only one real tuple is being returned, but it contains two values.  The comma indicates the use of tuple.

if __name__ == "__main__":
    main()
