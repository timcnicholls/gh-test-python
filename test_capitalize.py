# test_capitalize.py - test capitalization
import pytest


def capitalize_string(s):
    if not isinstance(s, str):
        raise TypeError("Please provide a string")
    return s.capitalize()


def test_capitalize_string():
    assert capitalize_string("test") == "Test"


def test_incorrect_argtype():
    with pytest.raises(TypeError, match="Please provide a string"):
        capitalize_string(1234)
