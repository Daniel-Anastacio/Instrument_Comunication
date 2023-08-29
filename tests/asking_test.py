from usecases.asking import asking


def test_asking():
    assert asking("yes") == True
    assert asking("no") == False
    assert asking("ANY") == False
