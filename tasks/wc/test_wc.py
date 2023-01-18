from wc import wc, wctotal

def test_empty():
    assert (0, 0, 0, 'null.txt')  == wc("null.txt")

def test_self():
    assert (48, 179, 1445, 'wc.py') == wc("wc.py")

def test_file():
    assert (3, 5, 28, 'file1.txt') == wc("file1.txt")

def test_wctotal():
    files1 = ["wc.py", "file1.txt"]
    files2 = ["wc.py", "null.txt"]

    list = wctotal(files1)
    item = list[len(list) - 1]
    assert(51, 184, 1473, 'Total') == item
    
    list = wctotal(files2)
    item = list[len(list) - 1]
    assert(48, 179, 1445, 'Total') == item