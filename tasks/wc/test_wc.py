from wc import wc, wctotal

def test_empty():
    assert (0, 0, 0)  == wc("null.txt")

def test_self():
    assert (57, 186, 1867) == wc("wc.py")

def test_file():
    assert (3, 5, 28) == wc("file1.txt")

def test_wctotal():
    files1 = ["wc.py", "file1.txt"]
    files2 = ["wc.py", "null.txt"]
    assert(60, 191, 1895) == wctotal(files1)
    assert(57, 186, 1867) == wctotal(files2)