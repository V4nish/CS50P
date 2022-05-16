from hello import hello


def test_argument():
    assert hello("David") == "hello, David"
    assert hello("Lyndon") == "hello, Lyndon"
    
    # Alternate method for multiple arguments
    for name in ["Bob", "Sid", "Bobby"]:
        assert hello(name) == f"hello, {name}"

def test_default():
    assert hello() == "hello, world"