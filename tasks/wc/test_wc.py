from wc import wc, wct

def test_empty():
    assert (0, 0, 0)  == wc("null.txt")

def test_self():
    assert (42, 151, 1497) == wc("wc.py")

def test_file():
    assert (3, 5, 28) == wc("file1.txt")