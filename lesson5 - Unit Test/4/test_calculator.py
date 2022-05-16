from calculator import square
#
# RUN FROM COMMAND PROMPT - pytest test_calculator.py
#
# 
# 
#  --> docs.pytest.org


def main():
    test_square()

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0


## Still getting into the habit
if __name__ == "__main__":
    main()
