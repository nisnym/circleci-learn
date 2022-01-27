# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(2,3) == 5
        assert Add(5,5) == 10
        assert Add(-1,1) == 0
        assert Add(6,6) == 12
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()