from reverse import *
import pytest

def test_success():
    assert reverse_sentence("Hello I am Kelton") == "Kelton am I Hello"
    assert reverse_sentence("A sentence") == "sentence A"

def test_single():
    assert reverse_sentence("word") == "word"

def test_failures():
    assert reverse_sentence("hello") == "olleh"