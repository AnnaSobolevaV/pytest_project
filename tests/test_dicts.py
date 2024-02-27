from utils import dicts


def test_get_val():
    assert dicts.get_val({1: 'one', 2: 'two', 3: 'three'}, 1, "test") == 'one'
    assert dicts.get_val({1: 'one', 2: 'two', 3: 'three'}, 5, "test1") == "test1"
    assert dicts.get_val({1: 'one', 2: 'two', 3: 'three'}, -5, "test1") == "test1"
    assert dicts.get_val({1: 'one', 2: 'two', 3: 'three'}, 'tt', "test1") == "test1"
    assert dicts.get_val({1: 'one', 2: 'two', 3: 'three'}, 0) == "git"
    assert dicts.get_val({1: 'one'}, 0) == "git"
    assert dicts.get_val({1: 'one'}, 1) == "one"
    assert dicts.get_val({1: 'one'}, 5, 'test2') == "test2"
    assert dicts.get_val({}, 0) == "git"
    assert dicts.get_val({}, 'test3') == "git"
    assert dicts.get_val({}, 5, 'test3') == "test3"
