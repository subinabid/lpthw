from wc import wc, wctotal


def test_empty():
    assert (0, 0, 0, "/Users/sabid/src/lpthw/tests/null.txt") == wc(
        "/Users/sabid/src/lpthw/tests/null.txt"
    )


def test_self():
    assert (51, 177, 1431, "/Users/sabid/src/lpthw/src/tasks/wc/wc.py") == wc(
        "/Users/sabid/src/lpthw/src/tasks/wc/wc.py"
    )


def test_file():
    assert (3, 3, 19, "/Users/sabid/src/lpthw/tests/file1.txt") == wc(
        "/Users/sabid/src/lpthw/tests/file1.txt"
    )


def test_wctotal():
    files1 = [
        "/Users/sabid/src/lpthw/src/tasks/wc/wc.py",
        "/Users/sabid/src/lpthw/tests/file1.txt",
    ]
    files2 = [
        "/Users/sabid/src/lpthw/src/tasks/wc/wc.py",
        "/Users/sabid/src/lpthw/tests/null.txt",
    ]

    list = wctotal(files1)
    item = list[len(list) - 1]
    assert (54, 180, 1450, "Total") == item

    list = wctotal(files2)
    item = list[len(list) - 1]
    assert (51, 177, 1431, "Total") == item
