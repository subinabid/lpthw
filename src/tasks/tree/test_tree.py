from tree import tree


def test_tree():
    # result = tree("../../../tests", 1)
    result = tree("/Users/sabid/src/lpthw/tests", 1)
    resultAsList = [(file.name, level) for file, level in result]
    sortedResult = sorted(resultAsList)
    predictedOutput = [
        ("Apple", 1),
        ("file2.txt", 1),
        ("file1.txt", 1),
        (".DS_Store", 1),
        ("file1 2.txt", 1),
        ("Beetle", 1),
        ("patternpad.jpeg", 1),
        ("test.txt", 1),
        ("null.txt", 1),
    ]

    sortedPredictedOutput = sorted(predictedOutput)
    assert sortedPredictedOutput == sortedResult


def test_tree_on_case():
    result, level = next(tree("/Users/sabid/src/lpthw/tests/Apple", 1))
    predicted_output = "Apple Sub"
    predicted_level = 1
    assert (predicted_output, predicted_level) == (result.name, level)
