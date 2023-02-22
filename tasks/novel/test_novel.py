import novel

def test_readme():
    temp = novel.topk('/usr/share/dict/README')
    empty = [(6, 'the'), (5, 'list'), (5, 'in'), (4, 'a'), (3, 'words')]
    assert empty == temp