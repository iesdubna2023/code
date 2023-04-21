import logging


def test_reverse(iter_homework):
    arg = [0, 1, 2, 3]
    expected = [3, 2, 1, 0]
    for surname, m in iter_homework(2):
        logging.info("Test reverse for %s", surname)
        r = m.reverse(arg)
        assert r == expected
        logging.info("Test reverse for %s: OK", surname)


def test_avglen(iter_homework):
    arg = ["aa", "aaaa", "aaaaaa"]
    expected = 4.0
    for surname, m in iter_homework(2):
        logging.info("Test avglen for %s", surname)
        r = m.avglen(arg)
        assert r == expected
        logging.info("Test avglen for %s: OK", surname)


def test_index(iter_homework):
    arg = ["her", "name", "is", "Masha", "Masha",
           "is", "a", "sister", "of", "Zhenya"]
    expected = {
        "her": 0,
        "name": 1,
        "is": [2, 5],
        "Masha": [3, 4],
        "a": 6,
        "sister": 7,
        "of": 8,
        "Zhenya": 9,
    }
    for surname, m in iter_homework(2):
        logging.info("Test index for %s", surname)
        r = m.index(arg)
        assert r == expected
        logging.info("Test index for %s: OK", surname)


def test_coincidence(iter_homework):
    arg1 = ["my", "name", "is", "Masha"]
    arg2 = ["my", "name", "is", "Zhenya", "some"]
    expected = ["my", "name", "is"]
    for surname, m in iter_homework(2):
        logging.info("Test coincidence for %s", surname)
        r = m.coincidence(arg1, arg2)
        assert set(r) == set(expected)
        logging.info("Test coincidence for %s: OK", surname)


def test_count(iter_homework):
    arg = ["aaa", "aaa", "bbb", "ccc", "bbb"]
    expected = {
        "aaa": 2,
        "bbb": 2,
        "ccc": 1,
    }
    for surname, m in iter_homework(2):
        logging.info("Test count for %s", surname)
        r = m.count(arg)
        assert r == expected
        logging.info("Test count for %s: OK", surname)


def test_lensort(iter_homework):
    for surname, m in iter_homework(2):
        logging.info("Test lensort for %s", surname)
        arg = ["abcd", "a", "ab", "abc", "bazinga", "bar"]
        expected = ["a", "ab", "abc", "bar", "abcd", "bazinga"]
        expected2 = ["a", "ab", "bar", "abc", "abcd", "bazinga"]
        r = m.lensort(arg)
        assert r == expected or r == expected2
        logging.info("Test lensort for %s: OK", surname)
