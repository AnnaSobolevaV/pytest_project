from utils import dicts
import pytest


@pytest.fixture
def dict1():
    return {1: 'one', 2: 'two', 3: 'three'}


@pytest.fixture
def dict2():
    return {'1': 'one'}


@pytest.fixture
def dict3():
    return {}


def test_get_val(dict1, dict2, dict3):
    assert dicts.get_val(collection=dict1, key=1, default="test") == 'one'
    assert dicts.get_val(dict1, 5, "test1") == "test1"
    assert dicts.get_val(dict1, -5, "test1") == "test1"
    assert dicts.get_val(dict1, 'tt', "test1") == "test1"
    assert dicts.get_val(dict1, 0) == "git"
    assert dicts.get_val(dict2, 0) == "git"
    assert dicts.get_val(dict2, '1') == "one"
    assert dicts.get_val(dict2, 5, 'test2') == "test2"
    assert dicts.get_val(dict3, 0) == "git"
    assert dicts.get_val(dict3, 'test3') == "git"
    assert dicts.get_val(dict3, 5, 'test3') == "test3"
