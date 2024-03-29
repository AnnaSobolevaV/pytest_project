from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([2, 3, 4, 5], 5, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 1) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], end=0) == []
    assert arrs.my_slice([1, 2, 3], start=-2, end=-1) == [2]
    assert arrs.my_slice([1, 2, 3], end=2) == [1, 2]
    assert arrs.my_slice([], end=2) == []
    assert arrs.my_slice([1, 2, 3], end=5) == [1, 2, 3]
