from tree import tree

def test_tree():
    result = tree(".", 1)
    resultAsList = [ (file.name, level) for file, level in result ]
    sortedResult =sorted(resultAsList)
    predictedOutput = [
        ('.pytest_cache', 1),
        ('Apple', 1),
        ('Beetle', 1),
        ('Empty Dir', 1),
        ('__pycache__', 1),
        ('file1.txt', 1),
        ('file2.txt', 1),
        ('test_tree.py', 1),
        ('tree.py', 1)]

    sortedPredictedOutput = sorted(predictedOutput)
    assert sortedPredictedOutput == sortedResult

def test_tree_on_case():
    result, level = next(tree("Apple", 1))
    predicted_output = "Apple Sub"
    predicted_level = 1
    assert (predicted_output, predicted_level) == (result.name, level) 