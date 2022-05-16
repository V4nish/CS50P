from calculator import square

def main():
    test_square()

def test_square():

    ## Now we've seen Errors, maybe not AssertionErrors, and dealt with them before - can we deal with them again?

    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 9")

    try:
        assert square(3) == 9
    except AssertionError:
        print("4 squared is not 9")

    try:
        assert square(-2) == 4
    except AssertionError:
        print("--2 squared is not 4")

    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared is not 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared is not 0")

##### TOO MUCH CODEZ!


## Still getting into the habit
if __name__ == "__main__":
    main()
