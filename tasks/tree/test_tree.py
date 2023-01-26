from tree import tree, print_tree, print_tree_item

def test_tree():
    info = tree()
    print (info)
    for i in info:
        print (i.name)
