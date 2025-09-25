import hello

def test_hello():
    assert hello.hello() == "Hello, CI/CD World - Update 1!"

def test_add():
    assert hello.add(2, 3) == 5
    assert hello.add(-1, 1) == 0
    assert hello.add(0, 0) == 0

if __name__ == "__main__":
    test_hello()
    test_add()
    print("All tests passed!")
