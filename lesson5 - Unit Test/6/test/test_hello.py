from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Lyndon") == "hello, Lyndon"



## MUST create __init__.py in test directory