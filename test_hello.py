#!/usr/bin/env python3

# Test the functions directly instead of importing as a module
def hello():
    return "Hello, CI/CD World - Update 1!"

def add(a, b):
    return a + b

def test_hello():
    result = hello()
    expected = "Hello, CI/CD World - Update 1!"
    assert result == expected, f"Expected '{expected}', but got '{result}'"
    print("✅ test_hello passed!")

def test_add():
    assert add(2, 3) == 5, "2 + 3 should equal 5"
    assert add(-1, 1) == 0, "-1 + 1 should equal 0"
    assert add(0, 0) == 0, "0 + 0 should equal 0"
    print("✅ test_add passed!")

if __name__ == "__main__":
    test_hello()
    test_add()
    print("🎉 All tests passed!")
