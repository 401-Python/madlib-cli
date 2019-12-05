from madlib import (get_keys,
                    get_responses,
                    read_file,
                    write_file,
                    remove_word_classes,
                    create_madlib)

import pytest

test_file = ('test_madlib.txt')
default_file = ('default.txt')
test_string = "I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}"


def test_read_file():
    with open(test_file) as f:
        expected = read_file(test_file)
        actual = f.read()
        assert expected == actual


def test_write_file():
    write_file(test_file, 'test')
    with open(test_file) as f:
        assert f.read() == 'test'


def test_get_keys():
    actual = get_keys(test_string)
    expected = ['Adjective', 'Adjective', 'A First Name', 'Past Tense Verb']
    assert actual == expected


def test_remove_word_classes():
    actual = remove_word_classes(test_string)
    expected = "I the {} and {} {} have {}"
    assert actual == expected

  
