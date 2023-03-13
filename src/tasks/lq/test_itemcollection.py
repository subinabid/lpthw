from itemcollection import Stack, Q, QEmpty, FileStack
from pytest import raises


def test_push():
    s = Stack()
    s.push(1)
    assert [1] == s.to_list()


def test_pop():
    a = Stack()
    b = Stack()
    b.push(1).push(2).push(3)
    assert None == a.pop()
    assert 3 == b.pop()


def test_enque():
    a = Q()
    a.enque(1)
    b = Q()
    b.enque(1).enque(2).enque(3)
    assert [1] == a.to_list()
    assert [1, 2, 3] == b.to_list()


def test_empty_deque():
    a = Q()
    with raises(QEmpty):
        a.deque()


def test_nonempty_deque():
    b = Q().enque(1).enque(2).enque(3)
    assert 1 == b.deque()


def test_file_push():
    s = FileStack()
    s.push("Cloudtest")
    with open(s.filename) as f:
        prediction = f.readlines()
        assert prediction[-1] == "Cloudtest\n"
